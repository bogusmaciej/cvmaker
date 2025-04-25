from flask import Flask, render_template, request, send_file, after_this_request
import cv_generator
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = {
            "personal_info": {},
            "education": [],
            "experience": [],
            "skills": [],
            "hoobies": []
        }
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        city = request.form["city"]
        description = request.form["description"]
        profession = request.form["profession"]
        schools = request.form.getlist('school')
        degrees = request.form.getlist('degree')
        majors = request.form.getlist('major')
        years_start = request.form.getlist('year_start')
        years_end = request.form.getlist('year_end')
        completeds = request.form.getlist('completed')
        education = []
        for i in range(len(schools)):
            edu_entry = {
                "school": schools[i],
                "degree": degrees[i],
                "major": majors[i],
                "year_start": years_start[i],
                "year_end": years_end[i],
                "completed": str(i) in completeds  # checkboxy są tricky
            }
            education.append(edu_entry)
        personal_info = {
                "name": name,
                "email": email,
                "phone": phone,
                "description": description,
                "city": city,
                "profession": profession
            }
        data["personal_info"] = personal_info
        data["education"] = education
        file_buffer = cv_generator.generate(data)
        
        return send_file(
            file_buffer,
            as_attachment=True,
            download_name=cv_generator.clear_filename(f"CV {name}.pdf"),
            mimetype='application/pdf'
        )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)