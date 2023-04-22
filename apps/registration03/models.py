from django.shortcuts import render
from wagtail.core.models import Page
from wagtail.core import hooks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.panels import (
    FieldPanel,
)
from wagtail.fields import RichTextField

class MyPage(RoutablePageMixin, Page):
    template = 'myapp/mypage.html'

    text = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("text", classname="full")]

    @route(r'^$')
    def default_view(self, request, *args, **kwargs):

        # Obtener el idioma preferido del usuario desde la variable de sesión
        idioma = request.session.get('idioma', 'es')

        # Obtener el contexto de la página
        context = self.get_context(request, *args, **kwargs)
        
        # Agregar cualquier contexto adicional para la vista en inglés
        context.update({
            'titulo': self.titulo_en_idioma(idioma),
            'contenido': self.contenido_en_idioma(idioma)
        })
        
        # lógica de vista para la ruta URL por defecto
        return render(request, self.template, context)

    @route(r'^es/$')
    def alternative_view_es(self, request, *args, **kwargs):
        # lógica de vista para la ruta URL alternativa
        # Obtener el idioma preferido del usuario desde la variable de sesión
        idioma = request.session.get('idioma', 'es')

        # Obtener el contexto de la página
        context = self.get_context(request, *args, **kwargs)
        
        # Agregar cualquier contexto adicional para la vista en inglés
        context.update({
            'titulo': self.titulo_en_idioma(idioma),
            'contenido': self.contenido_en_idioma(idioma)
        })
        
        # lógica de vista para la ruta URL por defecto
        return render(request, self.template, context)
    
    @route(r'^pt/$')
    def alternative_view_pt(self, request, *args, **kwargs):
        # lógica de vista para la ruta URL alternativa
        idioma = request.session.get('idioma', 'pt')

        # Obtener el contexto de la página
        context = self.get_context(request, *args, **kwargs)
        
        # Agregar cualquier contexto adicional para la vista en inglés
        context.update({
            'titulo': self.titulo_en_idioma(idioma),
            'contenido': self.contenido_en_idioma(idioma)
        })
        
        # lógica de vista para la ruta URL por defecto
        return render(request, self.template, context)
    
    @route(r'^en/$')
    def alternative_view_en(self, request, *args, **kwargs):
        # lógica de vista para la ruta URL alternativa
        idioma = request.session.get('idioma', 'en')

        # Obtener el contexto de la página
        context = self.get_context(request, *args, **kwargs)
        
        # Agregar cualquier contexto adicional para la vista en inglés
        context.update({
            'titulo': self.titulo_en_idioma(idioma),
            'contenido': self.contenido_en_idioma(idioma)
        })
        
        # lógica de vista para la ruta URL por defecto
        return render(request, self.template, context)
    
    def titulo_en_idioma(self, idioma):
        # Lógica para obtener el título de la página en el idioma especificado
        # Implementar según sea necesario
        if idioma == 'en':
            return 'Title in English'
        elif idioma == 'pt':
            return 'Titulo en Portugues'
        else:
            return 'Título en español'

    def contenido_en_idioma(self, idioma):
        # Lógica para obtener el contenido de la página en el idioma especificado
        # Implementar según sea necesario
        if idioma == 'en':
            return 'Content in English'
        elif idioma == 'pt':
            return 'Contenido en Portugues'
        else:
            return 'Contenido en español'

@hooks.register('register_page_types')
def register_my_page():
    return [MyPage]
