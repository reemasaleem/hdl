from docutils import nodes

def dokuwiki():
	def role(name, rawtext, text, lineno, inliner, options={}, content=[]):

		app = inliner.document.settings.env.app
		try:
			if not app.config.dokuwiki_url:
				raise AttributeError
		except AttributeError as err:
			raise ValueError('dokuwiki_url configuration value is not set (%s)' % str(err))
		path = text[text.find(':')+1:]
		name = path[path.rfind('/')+1:] if text.find(':') in [0, -1] else text[0:text.find(':')]
		url = app.config.dokuwiki_url + '/' + path
		node = nodes.reference(rawtext, name, refuri=url, **options)
		return [node], []
	return role

def setup(app):
	app.add_role("dokuwiki", dokuwiki())
	app.add_config_value('dokuwiki_url', None, 'env')

	return {
		'version': '0.1',
		'parallel_read_safe': True,
		'parallel_write_safe': True,
	}
