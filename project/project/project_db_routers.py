class DefaultRouter(object):
    apps =  ['admin', 'auth', 'contenttypes', 'sessions', 'messages', 'staticfiles', 'djcelery']
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.apps:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.apps:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.apps or \
           obj2._meta.app_label in self.apps:
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label in self.apps:
            return db == 'default'
        return None


class DataRouter(object):

    apps = ['home', 'services', 'about', 'contacts', 'parse', 'errors']

    def db_for_read(self, models, **hints):
        if models._meta.app_label in self.apps:
            return 'second'
        return None

    def db_for_write(self, models, **hints):
        if models._meta.app_label in self.apps:
            return 'second'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.apps or\
           obj2._meta.app_label in self.apps:
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label in self.apps:
            return db == 'second'
        return None
