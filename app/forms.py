# -*- coding: UTF-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class EventSearch(Form):
	event_name = StringField('event_name', validators=[DataRequired()])
	position = StringField('position', validators=[DataRequired()])
	location = SelectField('location', choices=[('Ha Noi', u'Hà Nội'), 
												('Ho chi minh', u'TP.Hồ Chí Minh'),
												('Nha trang', u'Nha Trang'),
												('Ho Chi Minh', u'Đà Nẵng'),
												('Hai Phong', u'Hải Phòng'),
												('Lam Dong', u'Lâm Đồng'),
												('Quang ninh', u'Quảng Ninhh'),
												('Nam dinh', u'Nam Định'),
												('Nghe an', u'Nghệ An'),])