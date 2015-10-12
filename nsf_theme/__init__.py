

def includeme(config):
    settings = config.registry.settings
    cache_max_age = int(settings.get('arche.cache_max_age', 60*60*24))
    config.add_static_view('_nsf_static', 'static', cache_max_age = cache_max_age)
    #Override templates
    config.override_asset(to_override='voteit.core:templates/overrides/',
                          override_with='nsf_theme:templates/overrides/')
