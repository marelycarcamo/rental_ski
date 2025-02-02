# views.py

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Arriendo, Equipo, Usuario, Categoria
from django.utils import timezone
from django.http import HttpResponseBadRequest



def index(request):
    # Obtener todos los equipos con estado 'disponible'
    equipos_disponibles = Equipo.objects.filter(estado='disponible')
    
    # Obtener todas las categorías para el dropdown
    categorias = Categoria.objects.all()
    
    context = {
        'equipos': equipos_disponibles,
        'categorias': categorias,
        'categoria_filtrada': 'todos',  # Por defecto, se muestran todos los equipos
    }
    
    return render(request, "index.html", context)



login_required
def equipo_list(request):
    # Obtener el valor del filtro de categoría del dropdown (por defecto será 'todos')
    categoria_filtrada = request.GET.get('categoria', 'todos')

    # Si no se ha seleccionado una categoría, mostrar todos los equipos disponibles
    if categoria_filtrada == 'todos' or not categoria_filtrada:
        equipos = Equipo.objects.filter(estado='disponible')
    else:
        # Filtrar por categoría y estado
        equipos = Equipo.objects.filter(estado='disponible', categoria__nombre=categoria_filtrada)

    # Obtener todas las categorías para el dropdown
    categorias = Categoria.objects.all()

    context = {
        'equipos': equipos,
        'categorias': categorias,
        'categoria_filtrada': categoria_filtrada,
    }

    return render(request, 'index.html', context)




@login_required
def arriendo_view(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    return render(request, 'arrendar.html', {'equipo': equipo})



# def login(request):
#     return redirect ('/accounts/login.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Usuario  # Importa tu modelo Usuario

def login_view(request):
    """
    Vista personalizada para manejar el login.
    Verifica el tipo de usuario y lo redirige a la página correspondiente.
    """
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Iniciar sesión
            login(request, user)

            # Verificar si el usuario tiene un perfil de Usuario
            try:
                usuario = Usuario.objects.get(user=user)
                tipo_usuario = usuario.tipo
            except Usuario.DoesNotExist:
                # Si no tiene perfil, redirigir al index (o a una página de error)
                return redirect('index')

            # Redirigir según el tipo de usuario
            if tipo_usuario == 'cliente':
                return redirect('index')  # Redirigir a la página de clientes
            elif tipo_usuario == 'operario':
                return redirect('arriendos')  # Redirigir a la página de operarios
            # elif user.is_superuser:
            #     return redirect('admin/')  # Redirigir al panel de administración
            else:
                return redirect('index')  # Redirigir a una página por defecto
        else:
            # Si la autenticación falla, mostrar un mensaje de error
            return render(request, 'registro/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        # Si no es una solicitud POST, mostrar el formulario de login
        return render(request, 'registro/login.html')


@login_required
def logout_view(request): 
    messages.success(request, "Has cerrado sesión exitosamente.")
    logout(request)  
    return redirect("index")  




from django.shortcuts import redirect

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        email = request.POST['email']
        tipo = request.POST['user_type']
    
        # Verifica si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe. Por favor, inicia sesión.")
            return redirect('login')  # Redirige al login si el usuario ya existe
        
        # Crear un nuevo usuario
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name)
        user.save()
        
        # Crear un perfil adicional en la tabla Usuario
        usuario = Usuario(
            user=user,
            tipo=tipo,
        )
        usuario.save()
        return redirect('login')
    return render(request, 'registro.html')




@login_required
def arrendar_view(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        if fecha:
            fecha = timezone.datetime.strptime(fecha, '%Y-%m-%d').date()
            if fecha < timezone.now().date():
                return HttpResponseBadRequest("La fecha no puede ser anterior a hoy.")
                # Guardar el arriendo en la base de datos


    # Obtener el usuario autenticado
    user = request.user

    # Obtener la instancia del modelo Usuario relacionada con este User
    usuario = get_object_or_404(Usuario, user=user)
    if request.method == "POST":
            # Crear un nuevo arriendo con la instancia de Usuario
            arriendo = Arriendo.objects.create(
                user=usuario,
                equipo=equipo,
                fecha=fecha,  
        
            )
            arriendo.save()
            # Cambiar el estado del equipo a arrendado
            equipo.estado = 'arrendado'
            equipo.save()

            # Mensaje de éxito
            messages.success(request, f'¡El equipo {equipo.nombre} ha sido arrendado exitosamente!')
            
            return redirect('equipo_list')
    return render(request, 'arrendar.html', {'equipo': equipo})



#En caso del que el usuario sea de tipo operario
@login_required
def vista_arriendos(request):
    try:
        # Obtener todos los registros de arriendo
        arriendos = Arriendo.objects.all()

        # Pasar los registros al template
        context = {
            'arriendos': arriendos
        }

        # Retornar el template con los datos
        return render(request, 'arriendos.html', context)
    
    except Exception as e:
        # Manejo de errores, opcionalmente puedes loguear o mostrar un mensaje de error
        print(f"Error: {e}")
        return render(request, 'arriendos.html', {'error': 'Hubo un problema al cargar los arriendos.'})



# Redes Sociales

def facebook_redirect(request):
    return redirect('https://web.facebook.com/antillancachile/?_rdc=1&_rdr#')

def instagram_redirect(request):
    return redirect('https://www.instagram.com/skiantillanca/')

def twitter_redirect(request):
    return redirect('https://x.com/AntillancaChile')

def youtube_redirect(request):
    return redirect('https://www.youtube.com/channel/UC_Am5BKnwMxi_3KieAFJnuA')


