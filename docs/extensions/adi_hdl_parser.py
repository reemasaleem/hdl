from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import Directive, directives
from sphinx.util.nodes import nested_parse_with_titles
from sphinx.util import logging
from ipyxact.ipyxact import Component
import os.path

logger = logging.getLogger(__name__)

class node_parameters(nodes.Structural, nodes.Element):
	pass

class directive_parameters(Directive):
	required_arguments = 0
	optional_arguments = 0
	final_argument_whitespace = True
	option_spec = {'path': directives.unchanged}
	has_content = True
	add_index = True
	current_doc = ''

	def warning(self, msg):
		logger.warning(msg + f" Current file: {self.current_doc}")
	def info(self, msg):
		logger.info(msg + f" Current file: {self.current_doc}")

	def recover_type(self, value):
		# Hackish method, cannot obtain spirit:format with ipyxact
		if value == 'true' or value == 'false':
			return 'Bool'
		try:
			int(value)
		except:
			return 'String'
		return 'Integer'

	def table_parameters(self, path, content, include_all):
		description = {}
		tag = ''
		for line in content:
			if line.startswith('* -'):
				tag = line[line.find('* -')+3:].split()[0]
				description[tag] = []
			else:
				description[tag].append(line)
		for tag in description:
			description[tag] = ' '.join(description[tag]).strip().replace('- ', '', 1)

		table = nodes.table()

		parameters = {}
		ip_name = path[path.rfind('/')+1:]
		file_1 = ip_name + '_hw.tcl'
		if not os.path.isfile(f"../{path}/{file_1}"):
			self.info(f"{file_1} does not exist, skipped.")
		with open(f"../{path}/{file_1}", 'r') as file:
			for line in file:
				line = line.strip()
				if line.startswith('ad_ip_parameter'):
					# Requires parsing, skip
					if line.find('$') != -1:
						continue
					line_ = line.split(' ', 4)
					if len(line_) == 4:
						line_.append('')
					_, name, type_, default, comment = line_
					comment = comment.replace('#','',1).strip()
					if comment != '' and comment[-1] != '.':
						comment += '.'
					parameters[name] = {'type': type_, 'default': default, 'comment': comment}

		file_2 = 'component.xml'
		if not os.path.isfile(f"../{path}/{file_2}"):
			self.info(f"{file_2} from {ip_name} does not exist, skipped.")
		else:
			component = Component()
			with open(f"../{path}/{file_2}", 'r') as file:
				component.load(file)
			for param in component.parameters.parameter:
				if param.name == 'Component_Name':
					continue
				type_ = self.recover_type(param.value)
				parameters[param.name] = {'type': type_, 'default': param.value, 'comment': ''}

		for tag in description:
			if tag not in parameters:
				self.warning(f"{tag} does not exist in {file_1} or {file_2}!")
			elif parameters[tag]['comment'] != '':
				description[tag] = ' '.join([parameters[tag]['comment'], description[tag]])

		if include_all is False:
			for tag in list(parameters):
				if tag not in description:
					del parameters[tag]

		tgroup = nodes.tgroup(cols=4)
		for _ in range(4):
			colspec = nodes.colspec(colwidth=1)
			tgroup.append(colspec)
		table += tgroup

		thead = nodes.thead()
		tgroup += thead
		row = nodes.row()

		for header_name in ["Name", "Description", "Type", "Default Value"]:
			entry = nodes.entry()
			entry += nodes.paragraph(text=header_name)
			row += entry

		thead.append(row)

		rows = []
		for key in parameters:
			row = nodes.row()
			entry = nodes.entry()
			entry += nodes.literal(text="{:s}".format(key))
			row += entry
			entry = nodes.entry()
			if key in description:
				rst = ViewList()
				rst.append(description[key], "virtual_"+path, 0)
				node = nodes.section()
				node.document = self.state.document
				nested_parse_with_titles(self.state, rst, node)
				entry += node
			else:
				entry += ''
			row += entry
			for tag in ['type', 'default']:
				entry = nodes.entry()
				entry += nodes.paragraph(text=parameters[key][tag].title())
				row += entry

			rows.append(row)

		tbody = nodes.tbody()
		tbody.extend(rows)
		tgroup += tbody

		return table

	def guess_path(self):
		path = self.current_doc
		for key in ['library', 'projects']:
			start_index = path.find(key)
			if start_index != -1:
				break

		end_index = path.rfind('.')
		if (path.rfind('/index')) != -1:
			end_index = path.rfind('/index')

		return path[start_index:end_index]

	def run(self):
		env = self.state.document.settings.env
		self.current_doc = env.doc2path(env.docname)

		node = node_parameters()

		if 'path' not in self.options:
			path = self.guess_path()
			if not os.path.isdir('../'+path):
				self.warning(f"Guessed path {path}, but it does not exist, set the path option explicitely!")
				return [ node ]
		else:
			path = self.options['path']
			if not os.path.isdir('../'+path):
				self.warning(f"Path {path} does not exist!")
				return [ node ]

		include_all = False
		if 'adi_hdl_parser_include_all' not in env.config:
			self.warning("adi_hdl_parser_include_all is not set!")
		elif env.config.adi_hdl_parser_include_all is True:
			include_all = True

		node_table = nodes.section(ids=["hdl-parameters"])

		node_table += self.table_parameters(path, self.content, include_all)
		node += node_table

		return [ node ]

def visit_node_parameters(self, node):
	pass

def depart_node_parameters(self, node):
	pass

def setup(app):
	app.add_directive('hdl-parameters', directive_parameters)
	app.add_node(node_parameters,
			html=(visit_node_parameters, depart_node_parameters),
			latex=(visit_node_parameters, depart_node_parameters),
			text=(visit_node_parameters, depart_node_parameters))

	app.add_config_value('adi_hdl_parser_include_all', False, 'env')

	return {
		'version': '0.1',
		'parallel_read_safe': True,
		'parallel_write_safe': True,
	}
