from cicip.models import Pesan

def get_dialog(request):
    dialog_list = Pesan.objects.filter(user=request.user)
    return { 'dialog_list' : dialog_list }
