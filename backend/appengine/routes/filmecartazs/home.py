from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.filmecartazs import rest
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
@no_csrf
def index():
    context = {
        'salvar_path': router.to_path(rest.save),
        'deletar_path': router.to_path(rest.delete),
        'editar_path': router.to_path(rest.update),
        'listar_path': router.to_path(rest.index)}
    return TemplateResponse(context)
