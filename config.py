class Config:
  DEBUG = False
  TESTING = False

  SECRET_KEY = "LKJHGFDSAasdfghjkl0987654321"

class ProductionConfig(Config):
  pass

class DevelopmentConfig(Config):
  DEBUG = True