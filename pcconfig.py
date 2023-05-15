import pynecone as pc

class PynebinConfig(pc.Config):
    pass

config = PynebinConfig(
    app_name="pynebin",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
