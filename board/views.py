from django.shortcuts import render, redirect
from .models import Message
from .forms import BoardForm

# Create your views here.

def index(request):
    if request.method == "POST":    #POSTリクエストが来たかどうか
        form = BoardForm(data=request.POST) #リクエストの内容を元にformを作成(form.pyの)
        if form.is_valid(): #formに値が入っていたら　←あってるかわからん
            Message.objects.create(message=form.cleaned_data['text'])   #model.pyのMessageオブジェクトを作成
                                                                        #form.cleaned_data['form.pyのほしいフィールド']でリクエストの内容を取得できる
            return redirect('board:index')
    else:
        form = BoardForm()  #POSTリクエスト来てなかったらただ単にフォームだけ作成

    context = { #templates/index.htmlの{{ 'フィールド名' }}に渡す値をここでまとめる
        'messages': Message.objects.all(),
        'form': form,
    }

    return render(request, 'board/index.html', context) #リクエスト、テンプレート、contextをまとめてクライアントに返す(Response)
