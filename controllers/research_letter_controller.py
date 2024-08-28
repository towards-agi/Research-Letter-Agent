from flask import render_template, request, redirect, url_for, flash
from services.letter_generator import generate_research_letter

def research_interest_advanced():
    if request.method == 'GET':
        return render_template('research_interest_advanced.html')

    elif request.method == 'POST':
        flash("Generating your research interest letter!")
        name = request.form.get('name')
        prof_name = request.form.get('prof_name')
        university = request.form.get('university')
        special_pref = request.form.get('special_pref')
        model = request.form.get('model')

        # Get the resume content from the textbox
        resume_content = request.form.get('resume')
        if not resume_content or resume_content.strip() == '':
            flash("Resume content cannot be empty.")
            return redirect(request.url)

        letters = generate_research_letter(name, prof_name, university, model, special_pref, resume_content)

        if not letters:
            flash("Failed to generate the letter.")
            return redirect(request.url)

        return render_template("showCL.html", cover_letter1=letters[0], cover_letter2=letters[1])

