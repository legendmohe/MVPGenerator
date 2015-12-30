#!/usr/bin/python

import os
import argparse
import datetime
import json
import os, errno

from jinja2 import Environment, FileSystemLoader

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(THIS_DIR, 'output')
MVP_DIR = os.path.join(OUTPUT_DIR, 'mvp') 
ENV = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def create_MPVView(package_name, author, ctime):
    out_path = os.path.join(MVP_DIR, 'MVPView.java')
    result = ENV.get_template('MVPView.java').render(
        package_name=package_name,
        author=author,
        create_time=ctime
    )
    with open(out_path, 'w') as f:
        f.write(result)

    print "create MVPView in path:", out_path

def create_MPVPresenter(package_name, author, ctime):
    out_path = os.path.join(MVP_DIR, 'MVPPresenter.java')
    result = ENV.get_template('MVPPresenter.java').render(
        package_name=package_name,
        author=author,
        create_time=ctime
    )
    with open(out_path, 'w') as f:
        f.write(result)

    print "create MVPPresenter in path:", out_path

def create_target_view(package_name, author, date_str, name):
    view_name = name.capitalize() + 'View'
    result = ENV.get_template('TemplateView.java').render(
        package_name=package_name,
        author=author,
        create_time=date_str,
        view_name = view_name
    )
    
    out_path = os.path.join(MVP_DIR, 'views')
    out_path = os.path.join(out_path, view_name + '.java')
    with open(out_path, 'w') as f:
        f.write(result)

    print "create view in path:", out_path
    return view_name

def create_target_presenter(package_name, author, date_str, name, vname):
    presenter_name = name.capitalize() + 'Presenter'
    result = ENV.get_template('TemplatePresenter.java').render(
        package_name=package_name,
        author=author,
        create_time=date_str,
        presenter_name = presenter_name,
        view_name = vname
    )

    out_path = os.path.join(MVP_DIR, 'presenters')
    out_path = os.path.join(out_path, presenter_name + '.java')
    with open(out_path, 'w') as f:
        f.write(result)

    print "create presenter in path:", out_path
    return presenter_name

def create_target_activity(package_name, author, date_str, name, pname, vname):
    activity_name = name.capitalize() + 'Activity'
    result = ENV.get_template('TemplateActivity.java').render(
        package_name=package_name,
        author=author,
        create_time=date_str,
        activity_name = activity_name,
        presenter_name = pname,
        view_name = vname
    )

    out_path = os.path.join(OUTPUT_DIR, activity_name + '.java')
    with open(out_path, 'w') as f:
        f.write(result)

    print "create activity in path:", out_path

def mkdir_dirs():
    mkdir_p(MVP_DIR)
    mkdir_p(os.path.join(MVP_DIR, 'presenters'))
    mkdir_p(os.path.join(MVP_DIR, 'views'))

def gen_with_template(package, author, date_str, target):
    name = target['name']
    gen_type = target['gen_type']

    vname = create_target_view(package, author, date_str, name)
    pname = create_target_presenter(package, author, date_str, name, vname)

    if gen_type.lower() == 'activity':
        create_target_activity(package, author, date_str, name, pname, vname)

def main(conf_file):
    conf = ""
    with open(conf_file, 'r') as f:
        conf = f.read()
    print "load conf:\n", conf

    conf_obj = json.loads(conf)
    package = conf_obj['package']
    author = conf_obj['author']

    mkdir_dirs()
    date_str = datetime.date.today().strftime('%y/%m/%d')
    create_MPVView(package, author, date_str)
    create_MPVPresenter(package, author, date_str)

    for target in conf_obj['target']:
        gen_with_template(package, author, date_str, target)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("conf", help="conf file")
    args = parser.parse_args()
    main(args.conf)

