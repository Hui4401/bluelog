import os
import sys


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_LANGUAGE = 'zh-cn'
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'    # 处理图片上传的视图函数的url或端点值
    CKEDITOR_UPLOAD_PATH = os.path.join(basedir, 'uploads')

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('admin', MAIL_USERNAME)

    BLOG_POST_PER_PAGE = 10
    BLOG_MANAGE_POST_PER_PAGE = 15
    BLOG_COMMENT_PER_PAGE = 10

    # {'主题名': 'css文件名'}
    BLOG_THEMES = {
        'Perfect Blue': 'perfect_blue',
        'Black Swan': 'black_swan'
    }
    BLOG_THEME = list(BLOG_THEMES.keys())[0]


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'data.db'))


config = {
    'base': BaseConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
