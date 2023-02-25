from django.shortcuts import redirect



def auth_doctor(func):
    def wrap(request, *args, **kwargs):
        if 'doctor' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:user_type')
            
    return wrap



def auth_patient(func):
    def wrap(request, *args, **kwargs):
        if 'patient' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:user_type')
            
    return wrap




def auth_admin(func):
    def wrap(request, *args, **kwargs):
        if 'admin' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:user_type')
            
    return wrap

def auth_staff(func):
    def wrap(request, *args, **kwargs):
        if 'staff' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:user_type')
            
    return wrap