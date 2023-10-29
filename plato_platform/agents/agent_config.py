import autogen

# build the gpt_configuaration object
# base_configuration
base_config = {
    "use_cache": False,
    "temperature": 0,
    "config_list": autogen.config_list_from_models(["gpt-4"]),
    "request_timeout": 120,
}
