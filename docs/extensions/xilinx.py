from docutils import nodes

def xilinx():
	def role(name, rawtext, text, lineno, inliner, options={}, content=[]):

		app = inliner.document.settings.env.app
		try:
			if not app.config.git_org_url:
				raise AttributeError
		except AttributeError as err:
			raise ValueError('xilinx_url configuration value is not set (%s)' % str(err))
		name = text[text.rfind('/')+1:] if text.find(':') in [0, -1] else text[0:text.find(':')]
		path = text[text.find(':')+1:]
		url = app.config.xilinx_url + '/' + path
		node = nodes.reference(rawtext, name, refuri=url, **options)
		return [node], []
	return role

def setup(app):
	app.add_role("xilinx", xilinx())
	app.add_config_value('xilinx_url', None, 'env')

	return {
		'version': '0.1',
		'parallel_read_safe': True,
		'parallel_write_safe': True,
	}
