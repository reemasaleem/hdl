from docutils import nodes

def datasheet():
	def role(name, rawtext, text, lineno, inliner, options={}, content=[]):

		app = inliner.document.settings.env.app
		try:
			if not app.config.datasheet_url:
				raise AttributeError
		except AttributeError as err:
			raise ValueError('datasheet_url configuration value is not set (%s)' % str(err))
		if text.find(':') in [0, -1]:
			url = app.config.datasheet_url + '/' + part_id + '.pdf'
		else:
			anchor = text[text.find(':')+1:]
			part_id = text[0:text.find(':')]
			url = app.config.datasheet_url + '/' + part_id + '.pdf#' + anchor
		node = nodes.reference(rawtext, part_id + " datasheet", refuri=url, **options)
		return [node], []
	return role

def setup(app):
	app.add_role("datasheet", datasheet())
	app.add_config_value('datasheet_url', None, 'env')

	return {
		'version': '0.1',
		'parallel_read_safe': True,
		'parallel_write_safe': True,
	}
