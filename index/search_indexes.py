# coding=utf-8
from haystack import indexes
from .models import Goods


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Goods

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

"""
    4.创建索引
    如果你想针对某个app例如mainapp做全文检索，则必须在mainapp的目录下面建立search_indexes.py文件，文件名不能修改。内容如下：
        import datetime
        from haystack import indexes
        from myapp.models import Note

        class NoteIndex(indexes.SearchIndex, indexes.Indexable):
            text = indexes.CharField(document=True, use_template=True)

            author = indexes.CharField(model_attr='user')
            pub_date = indexes.DateTimeField(model_attr='pub_date')

            def get_model(self):
                return Note

            def index_queryset(self, using=None):
                "Used when the entire index for model is updated."
                return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

        每个索引里面必须有且只能有一个字段为document=True，这代表haystack 和搜索引擎将使用此字段的内容作为索引进行检索(primary field)。其他的字段只是附属的属性，方便调用，并不作为检索数据。

            注意：如果使用一个字段设置了document=True，则一般约定此字段名为text，这是在SearchIndex类里面一贯的命名，以防止后台混乱，当然名字你也可以随便改，不过不建议改。

        并且，haystack提供了use_template=True在text字段，这样就允许我们使用数据模板去建立搜索引擎索引的文件，使用方便（官方推荐，当然还有其他复杂的建立索引文件的方式，目前我还不知道），数据模板的路径为yourapp/templates/search/indexes/yourapp/note_text.txt，例如本例子为blog/templates/search/indexes/blog/note_text.txt文件名必须为要索引的类名_text.txt,其内容为

        {{ object.title }}
        {{ object.user.get_full_name }}
        {{ object.body }}

        这个数据模板的作用是对Note.title, Note.user.get_full_name,Note.body这三个字段建立索引，当检索的时候会对这三个字段做全文检索匹配。

    """