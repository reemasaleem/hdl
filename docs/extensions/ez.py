from docutils import nodes
import subprocess

def ez():
	def role(name, rawtext, text, lineno, inliner, options={}, content=[]):

		app = inliner.document.settings.env.app
		try:
			if not app.config.part_url:
				raise AttributeError
		except AttributeError as err:
			raise ValueError('ez_url configuration value is not set (%s)' % str(err))
		url = app.config.ez_url + '/' + text
		node = nodes.reference(rawtext, "EngineerZone", refuri=url, **options)
		return [node], []
	return role

def setup(app):
	app.add_role("ez", ez())
	app.add_config_value('ez_url', None, 'env')

	return {
		'version': '0.1',
		'parallel_read_safe': True,
		'parallel_write_safe': True,
	}
