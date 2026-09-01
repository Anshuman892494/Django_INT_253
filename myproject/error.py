from django.http import HttpResponse

def handler404(request, exception):
    html_content = """
    <div style="text-align: center; margin-top: 50px; font-family: Arial, sans-serif;">
        <h1 style="color: #ff4c4c; font-size: 50px;">Page Nhi Mil rha - Chhor de Padhai 🫩🫩🫩</h1>
    </div>
    """
    return HttpResponse(html_content, status=404)


def handler500(request, *args, **argv):
    html_content = """
    <div style="text-align: center; margin-top: 50px; font-family: Arial, sans-serif;">
        <h1 style="color: #ff4c4c; font-size: 50px;">500 - Server Error 💥</h1>
        <h2>Bhai Code Check kr, server crash ho gaya! 🫩🫩🫩</h2>
    </div>
    """
    return HttpResponse(html_content, status=500)
