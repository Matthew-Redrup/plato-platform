import autogen
from plato_platform.agents import agent_config


# Create our terminate msg function
def is_termination_msg(content):
    have_content = content.get("content", None) is not None
    if have_content and "APPROVED" in content["content"]:
        return True
    return False


USER_PROXY_PROMPT = ""
HOST_PROMPT = ""

# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="User_Proxy",
    system_message=USER_PROXY_PROMPT,
    code_execution_config=False,
    human_input_mode="ALWAYS",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
)
# create a HostAgent instance named "host"
host = autogen.AssistantAgent(
    name="Host",
    system_message=HOST_PROMPT,
    llm_config=agent_config.base_config,
    code_execution_config=False,
    human_input_mode="NEVER",
)
