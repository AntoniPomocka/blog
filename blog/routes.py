from flask import render_template, request, redirect, url_for, flash
from blog import app, db
from blog.models import Entry
from blog.forms import EntryForm

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
                flash('Nowy wpis został dodany!', 'success')
            else:
                entry.title = form.title.data
                entry.body = form.body.data
                entry.is_published = form.is_published.data
                flash('Wpis został zaktualizowany!', 'success')
            db.session.commit()
            return redirect(url_for('index'))
        else:
            errors = form.errors
            flash('Błąd w formularzu, sprawdź wprowadzone dane.', 'danger')

    return render_template('entry_form.html', form=form, errors=errors)

@app.route('/')
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", all_posts=all_posts)

@app.route('/new-post', methods=['GET', 'POST'])
def create_entry():
    return manage_entry()

@app.route('/edit-post/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    return manage_entry(entry_id=entry_id)