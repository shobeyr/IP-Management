# app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from .models import Group, IP  # وارد کردن مدل‌ها بعد از ایجاد db
from . import db
from .utils import validate_ip

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    groups = Group.query.all()
    ips = IP.query.all()
    return render_template('index.html', groups=groups, ips=ips)

@main_bp.route('/add_group', methods=['POST'])
def add_group():
    name = request.form.get('group_name')
    if name:
        group = Group(name=name)
        db.session.add(group)
        db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/add_ip', methods=['POST'])
def add_ip():
    group_id = request.form.get('group_id')
    server_name = request.form.get('server_name')
    ip_public = request.form.get('ip_public')
    ip_private = request.form.get('ip_private')
    dc = request.form.get('dc')
    description = request.form.get('description')

    if not validate_ip(ip_public) or not validate_ip(ip_private):
        return "Invalid IP format", 400

    new_ip = IP(
        group_id=group_id,
        server_name=server_name,
        ip_public=ip_public,
        ip_private=ip_private,
        dc=dc,
        description=description
    )
    db.session.add(new_ip)
    db.session.commit()
    return redirect(url_for('main.index'))
