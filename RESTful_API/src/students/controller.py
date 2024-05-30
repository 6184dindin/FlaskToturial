from flask import request
from flask_restful import Resource,abort
from ..models import *

# Tạo instances của StudentSchema
student_schema = StudentsSchema()
students_schema = StudentsSchema(many=True)

# Tạo resource để xử lý các phương thức GET và POST cho nguồn 'Students'
class StudentResource(Resource):
    # Xử lý phương thức GET
    def get(self, student_id=None):
        if student_id:
            # Lấy thông tin của một sinh viên cụ thể dựa trên student_id
            student = Students.query.get_or_404(student_id)
            return student_schema.dump(student)
        else:
            # Lấy tất cả sinh viên
            students = Students.query.all()
            return students_schema.dump(students)

    # Xử lý phương thức POST
    def post(self):
        # Lấy dữ liệu từ request
        data = request.json
        # Kiểm tra xem dữ liệu có chứa trường 'name' hay không
        if 'name' not in data:
            abort(400, message="Missing 'name' in request data")

        # Tạo một sinh viên mới
        new_student = Students(name=data['name'])
        # Thêm sinh viên vào cơ sở dữ liệu
        db.session.add(new_student)
        db.session.commit()

        return student_schema.dump(new_student), 201  # Trả về dữ liệu của sinh viên mới với status code 201 (Created)