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

        # Handling resume upload
        resume_file = request.files.get('resume')
        if not resume_file or resume_file.filename == '':
            flash("No selected file or no file part")
            return redirect(request.url)

        resume_content = resume_file.read().decode('utf-8')  # Assuming resume is in text format

        letters = generate_research_letter(name, prof_name, university, model, special_pref, resume_content)
        if not letters:
            flash("Failed to generate the letter.")
            return redirect(request.url)

        return render_template("showCL.html", cover_letter1=letters[0], cover_letter2=letters[1], total_tokens=52013124)
