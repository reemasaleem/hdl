from docutils import nodes
import subprocess

def part():
	def role(name, rawtext, text, lineno, inliner, options={}, content=[]):

		app = inliner.document.settings.env.app
		try:
			if not app.config.part_url:
				raise AttributeError
		except AttributeError as err:
			raise ValueError('part_url configuration value is not set (%s)' % str(err))
		part_name = text[text.find(':')+1:]
		part_id = part_name if text.find(':') in [0, -1] else text[0:text.find(':')]
		url = app.config.part_url + '/' + part_id + '.html'
		node = nodes.reference(rawtext, part_name, refuri=url, **options)
		return [node], []
	return role

def setup(app):
	app.add_role("part", part())
	app.add_config_value('part_url', None, 'env')

	return {
		'version': '0.1',
		'parallel_read_safe': True,
		'parallel_write_safe': True,
	}
