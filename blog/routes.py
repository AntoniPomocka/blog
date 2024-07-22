from flask import render_template, request, redirect, url_for, flash, session
from blog import app, db
from blog.models import Entry
from blog.forms import EntryForm, LoginForm
import functools

def login_required(view_func):
    @functools.wraps(view_func)
    def check_permissions(*args, **kwargs):
        if session.get('logged_in'):
            return view_func(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return check_permissions

def manage_entry(entry_id=None):
    entry = Entry.query.filter_by(id=entry_id).first() if entry_id else None
    form = EntryForm(obj=entry)
    errors = None

    if request.method == 'POST':
        if form.validate_on_submit():
            if entry is None:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data
                )
                db.session.add(entry)
                if entry.is_published:
                    flash('Nowy wpis został dodany!', 'success')
                else:
                    flash('Nowy szkic został dodany!', 'info')
            else:
                entry.title = form.title.data
                entry.body = form.body.data
                entry.is_published = form.is_published.data
                if entry.is_published:
                    flash('Wpis został zaktualizowany!', 'success')
                else:
                    flash('Szkic został zaktualizowany!', 'info')
            db.session.commit()
            return redirect(url_for('index'))
        else:
            errors = form.errors
            flash('Błąd w formularzu, sprawdź wprowadzone dane.', 'danger')

    return render_template('entry_form.html', form=form, errors=errors, entry_id=entry_id)

@app.route('/')
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", all_posts=all_posts)

@app.route('/new-post', methods=['GET', 'POST'])
@login_required
def create_entry():
    return manage_entry()

@app.route('/edit-post/<int:entry_id>', methods=['GET', 'POST'])
@login_required
def edit_entry(entry_id):
    return manage_entry(entry_id=entry_id)

@app.route('/post/<int:entry_id>', methods=['GET'])
def show_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    return render_template("show_entry.html", entry=entry)

@app.route('/delete-post/<int:entry_id>', methods=['POST'])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    db.session.delete(entry)
    db.session.commit()
    flash('Wpis został usunięty.', 'success')
    return redirect(url_for('index'))

@app.route('/drafts/', methods=['GET'])
@login_required
def list_drafts():
    draft_posts = Entry.query.filter_by(is_published=False).order_by(Entry.pub_date.desc())
    return render_template("drafts.html", draft_posts=draft_posts)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors = None
    next_url = request.args.get('next')
    if request.method == 'POST':
        if form.validate_on_submit():
            session['logged_in'] = True
            session.permanent = True
            flash('Zalogowano pomyślnie.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            errors = form.errors
    return render_template("login_form.html", form=form, errors=errors)

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.clear()
        flash('Wylogowano pomyślnie.', 'success')
    return redirect(url_for('index'))