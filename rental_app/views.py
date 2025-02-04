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
                return redirect('arriendo')  # Redirigir a la página de operarios
            # elif user.is_superuser:
            #     return redirect('admin/')  # Redirigir al panel de administración
            else:
                return redirect('index')  # Redirigir a una página por defecto
        else:
            # Si la autenticación falla, mostrar un mensaje de error
            return render(request, 'registration/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        # Si no es una solicitud POST, mostrar el formulario de login
        return render(request, 'registration/login.html')


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






from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Equipo, Usuario, Arriendo
from .forms import ArrendarEquipoForm  # Importamos nuestro formulario

@login_required
def arrendar_view(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    user = request.user
    usuario = get_object_or_404(Usuario, user=user)

    if request.method == 'POST':
        form = ArrendarEquipoForm(request.POST)  # Usamos el formulario
        
        if form.is_valid():
            # Los datos ya están validados aquí
            fecha = form.cleaned_data['fecha']

            # Crear arriendo
            arriendo = Arriendo.objects.create(
                user=usuario,
                equipo=equipo,
                fecha=fecha,
            )

            # Actualizar estado del equipo
            equipo.estado = 'arrendado'
            equipo.save()

            messages.success(request, f'¡{equipo.nombre} arrendado exitosamente!')
            return redirect('arrendar', equipo.id)

    else:  # Método GET
        form = ArrendarEquipoForm()  # Formulario vacío

    return render(request, 'arrendar.html', {
        'equipo': equipo,
        'form': form  # Pasamos el formulario al template
    })












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
        return render(request, 'arriendo.html', context)
    
    except Exception as e:
        # Manejo de errores, opcionalmente puedes loguear o mostrar un mensaje de error
        print(f"Error: {e}")
        return render(request, 'arriendo.html', {'error': 'Hubo un problema al cargar los arriendos.'})





# from django.shortcuts import get_object_or_404, redirect
# from django.contrib import messages
# from .models import Arriendo  # Asegúrate de importar el modelo Arriendo

def comentario_arriendo_view(request, arriendo_id):
    if request.method == 'POST':
        # Obtener el arriendo específico por su ID
        arriendo = get_object_or_404(Arriendo, id=arriendo_id)
        
        # Obtener los datos del formulario
        observacion = request.POST.get('observacion')
        danado = request.POST.get('danado') == 'True'  # Convertir a booleano
        
        # Actualizar los campos del arriendo
        arriendo.observacion = observacion
        arriendo.danado = danado
        arriendo.save()
        
        # Mensaje de éxito
        messages.success(request, 'Comentario y estado de daño actualizados correctamente.')
        
        # Redirigir a la página de arriendos o a donde sea necesario
        return redirect('arriendo')  # Cambia 'nombre_de_la_url_de_arriendos' por la URL a la que quieres redirigir
    
    # Si no es POST, redirigir a la página de arriendos
    return redirect('arriendo')












# Redes Sociales

def facebook_redirect(request):
    return redirect('https://web.facebook.com/antillancachile/?_rdc=1&_rdr#')

def instagram_redirect(request):
    return redirect('https://www.instagram.com/skiantillanca/')

def twitter_redirect(request):
    return redirect('https://x.com/AntillancaChile')

def youtube_redirect(request):
    return redirect('https://www.youtube.com/channel/UC_Am5BKnwMxi_3KieAFJnuA')


