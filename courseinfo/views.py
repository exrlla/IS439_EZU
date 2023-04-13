from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from courseinfo.forms import InstructorForm, SectionForm, CourseForm, SemesterForm, RegistrationForm, StudentForm
from courseinfo.models import (
    Instructor,
    Section,
    Course,
    Semester,
    Student,
    Registration,
)
from courseinfo.utils import PageLinksMixin


class InstructorList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Instructor


class InstructorDetail(DetailView):
    model = Instructor

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        instructor = self.get_object()
        section_list = instructor.sections.all()
        context['section_list'] = section_list
        return context


class InstructorCreate(CreateView):
    form_class = InstructorForm
    model = Instructor


class InstructorUpdate(UpdateView):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseinfo/instructor_form_update.html'


class InstructorDelete(View):

    def get(self, request, pk):
        instructor = self.get_object(pk)
        sections = instructor.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/instructor_refuse_delete.html',
                {'instructor': instructor,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/instructor_confirm_delete.html',
                {'instructor': instructor}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Instructor,
            pk=pk)

    def post(self, request, pk):
        instructor = self.get_object(pk)
        instructor.delete()
        return redirect('courseinfo_instructor_list_urlpattern')


class SectionList(ListView):
    model = Section


class SectionDetail(DetailView):
    model = Section

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        section = self.get_object()
        semester = section.semester
        course = section.course
        instructor = section.instructor
        registration_list = section.registrations.all()
        context['semester'] = semester
        context['course'] = course
        context['instructor'] = instructor
        context['registration_list'] = registration_list
        return context


class SectionCreate(CreateView):
    form_class = SectionForm
    model = Section


class SectionUpdate(UpdateView):
    form_class = SectionForm
    model = Section
    template_name = 'courseinfo/section_form_update.html'


class SectionDelete(View):

    def get(self, request, pk):
        section = self.get_object(pk)
        registrations = section.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/section_refuse_delete.html',
                {'section': section,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/section_confirm_delete.html',
                {'section': section}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Section,
            pk=pk)

    def post(self, request, pk):
        section = self.get_object(pk)
        section.delete()
        return redirect('courseinfo_section_list_urlpattern')


class CourseList(ListView):
    model = Course


class CourseDetail(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        name = course.course_name
        number = course.course_number
        section_list = course.sections.all()
        context['name'] = name
        context['number'] = number
        context['section_list'] = section_list
        return context


class CourseCreate(CreateView):
    form_class = CourseForm
    model = Course


class CourseUpdate(UpdateView):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'


class CourseDelete(View):

    def get(self, request, pk):
        course = self.get_object(pk)
        sections = course.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/course_refuse_delete.html',
                {'course': course,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/course_confirm_delete.html',
                {'course': course}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Course,
            pk=pk)

    def post(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return redirect('courseinfo_course_list_urlpattern')


class SemesterList(ListView):
    model = Semester


class SemesterDetail(DetailView):
    model = Semester

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        semester = self.get_object()
        section_list = semester.sections.all()
        context['section_list'] = section_list
        return context


class SemesterCreate(CreateView):
    form_class = SemesterForm
    model = Semester


class SemesterUpdate(UpdateView):
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'


class SemesterDelete(View):

    def get(self, request, pk):
        semester = self.get_object(pk)
        sections = semester.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/semester_refuse_delete.html',
                {'semester': semester,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/semester_confirm_delete.html',
                {'semester': semester}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Semester,
            pk=pk)

    def post(self, request, pk):
        semester = self.get_object(pk)
        semester.delete()
        return redirect('courseinfo_semester_list_urlpattern')


class StudentList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Student


class StudentDetail(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        student = self.get_object()
        registration_list = student.registrations.all()
        context['registration_list'] = registration_list
        return context


class StudentCreate(CreateView):
    form_class = StudentForm
    model = Student


class StudentUpdate(UpdateView):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'


class StudentDelete(View):

    def get(self, request, pk):
        student = self.get_object(pk)
        registrations = student.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/student_refuse_delete.html',
                {'student': student,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/student_confirm_delete.html',
                {'student': student}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Section,
            pk=pk)

    def post(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return redirect('courseinfo_student_list_urlpattern')


class RegistrationList(ListView):
    model = Registration


class RegistrationDetail(DetailView):
    model = Registration

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        registration = self.get_object()
        section = registration.section
        student = registration.student

        context['section'] = section
        context['student'] = student
        return context


class RegistrationCreate(CreateView):
    form_class = RegistrationForm
    model = Registration


class RegistrationUpdate(UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'


class RegistrationDelete(View):

    def get(self, request, pk):
        registration = self.get_object(pk)
        return render(
            request,
            'courseinfo/registration_confirm_delete.html',
            {'registration': registration}
        )

    def get_object(self, pk):
        registration = get_object_or_404(
            Registration,
            pk=pk
        )
        return registration

    def post(self, request, pk):
        registration = self.get_object(pk)
        registration.delete()
        return redirect('courseinfo_registration_list_urlpattern')
