class opdsTemplate():
    def __init__(self,charset='utf-8'):
       self.response_header=('Content-Type','text/xml; charset='+charset)

       self.agregate_authors=('<author><name>%(last_name)s %(first_name)s</name></author>')
       self.agregate_authors_link=('<link href="%(modulepath)s?id=22%(author_id)s" rel="related" type="application/atom+xml;profile=opds-catalog" title="Все книги %(last_name)s %(first_name)s" />')
       self.agregate_genres='<category term="%(genre)s" label="%(genre)s" />'
       self.agregate_genres_link=''
       self.agregate_series=''
       self.agregate_series_link=''

       self.document_page_header_style=''
       self.document_page_header=('<?xml version="1.0" encoding="%(charset)s"?>'
                               '<feed xmlns="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/terms/" xmlns:os="http://a9.com/-/spec/opensearch/1.1/" xmlns:opds="http://opds-spec.org/2010/catalog">'
                               '<id>%(page_id)s</id>'
                               '<title>%(page_title)s</title>'
                               '<subtitle>%(site_subtitle)s</subtitle>'
                               '<updated>%(page_updated)s</updated>'
                               '<icon>%(site_icon)s</icon>'
                               '<author><name>%(site_author)s</name><uri>%(site_url)s</uri><email>%(site_email)s</email></author>'
                               '<link type="application/atom+xml" rel="start" href="%(modulepath)s?id=00"/>')
       self.document_page_footer='</feed>'
       self.document_mainmenu_std=('<link href="%(modulepath)s?id=09" rel="search" type="application/opensearchdescription+xml" />'
                               '<link href="%(modulepath)s?searchTerm={searchTerms}" rel="search" type="application/atom+xml" />'
                               '<entry>'
                               '<title>По каталогам</title>'
                               '<content type="text">Каталогов: %(cat_num)s, книг: %(book_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=01"/>'
                               '<id>id:01</id></entry>'
                               '<entry>'
                               '<title>По авторам</title>'
                               '<content type="text">Авторов: %(author_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(alphabet_id)s02"/>'
                               '<id>id:02</id></entry>'
                               '<entry>'
                               '<title>По наименованию</title>'
                               '<content type="text">Книг: %(book_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(alphabet_id)s03"/>'
                               '<id>id:03</id></entry>'
                               '<entry>'
                               '<title>По Жанрам</title>'
                               '<content type="text">Жанров: %(genre_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=04"/>'
                               '<id>id:04</id></entry>'
                               '<entry>'
                               '<title>По Сериям</title>'
                               '<content type="text">Серий: %(series_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(alphabet_id)s06"/>'
                               '<id>id:06</id></entry>'
                               )
       self.document_mainmenu_new=('<entry>'
                               '<title>Новинки за %(new_period)s суток</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=05"/>'
                               '<id>id:05</id></entry>'
                               )
       self.document_mainmenu_shelf=('<entry>'
                               '<title>Книжная полка для %(user)s</title>'
                               '<content type="text">Книг: %(shelf_book_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=08"/>'
                               '<id>id:08</id></entry>'
                               )
       self.document_newmenu=('<entry>'
                               '<title>Все новинки за %(new_period)s суток</title>'
                               '<content type="text">Новых книг: %(newbook_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(alphabet_id)s03&amp;news=1"/>'
                               '<id>id:03:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по авторам</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(alphabet_id)s02&amp;news=1"/>'
                               '<id>id:02:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по Жанрам</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=04&amp;news=1"/>'
                               '<id>id:04:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по Сериям</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(alphabet_id)s06&amp;news=1"/>'
                               '<id>id:06:news</id></entry>'
                               )
       self.document_authors_submenu=('<entry>'
                               '<title>Книги по сериям</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=31%(author_id)s"/>'
                               '<id>id:31:authors</id></entry>'
                               '<entry>'
                               '<title>Книги вне серий</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=34%(author_id)s"/>'
                               '<id>id:32:authors</id></entry>'
                               '<entry>'
                               '<title>Книги по алфавиту</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=33%(author_id)s"/>'
                               '<id>id:33:authors</id></entry>'
                               )

       self.document_alphabet_menu=('<entry><title>А..Я (РУС)</title><id>alpha:1</id><link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(iid)s&amp;alpha=1%(nl)s"/></entry>'
                                    '<entry><title>0..9 (Цифры)</title><id>alpha:2</id><link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(iid)s&amp;alpha=2%(nl)s"/></entry>'
                                    '<entry><title>A..Z (ENG)</title><id>alpha:3</id><link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(iid)s&amp;alpha=3%(nl)s"/></entry>'
                                    '<entry><title>Другие Символы</title><id>alpha:4</id><link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(iid)s&amp;alpha=4%(nl)s"/></entry>'
                                    '<entry><title>Показать все</title><id>alpha:5</id><link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(iid)s&amp;alpha=5%(nl)s"/></entry>'
                                    )

       self.document_page_control_prev=('<link type="application/atom+xml;profile=opds-catalog;kind=acquisition" rel="prev" title="Previous Page" href="%(modulepath)s?id=%%(link_id)s&amp;page=%(page)s" />'
                               )
       self.document_page_control_next=('<link type="application/atom+xml;profile=opds-catalog;kind=acquisition" rel="next" title="Next Page" href="%(modulepath)s?id=%%(link_id)s&amp;page=%(page)s" />'
                               )

       self.document_entry_nav_start='<entry>'
       self.document_entry_nav_title=('<title>%(e_title)s</title>'
                               '<updated>%(e_date)s</updated>'
                               '<id>id:%(e_id)s</id>')
       self.document_entry_nav_link=('<link type="application/atom+xml" rel="alternate" href="%(modulepath)s?id=%(link_id)s%(nl)s"/>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=acquisition" rel="subsection" href="%(modulepath)s?id=%(link_id)s%(nl)s"/>'
                               )
       self.document_entry_nav_info=('<content type="text">%(e_nav_info)s</content>')
       self.document_entry_nav_finish='</entry>>'

       self.document_entry_acq_start='<entry>'
       self.document_entry_acq_link_start=''
       self.document_entry_acq_book_title=('<title>%(e_title)s</title>'
                               '<updated>%(e_date)s</updated>'
                               '<id>id:%(e_id)s</id>')
       self.document_entry_acq_book_link_alternate=('<link type="application/%(format)s" rel="alternate" href="%(modulepath)s?id=91%(item_id)s"/>'
                               )
       self.document_entry_acq_book_link=('<link type="application/%(format)s" href="%(modulepath)s?id=%(id)s%(item_id)s" rel="http://opds-spec.org/acquisition" />'
                               )
       self.document_entry_acq_link_finish=''

       self.document_entry_acq_info_start=''

       self.document_entry_acq_info_cover=('<link href="%(modulepath)s?id=99%(item_id)s" rel="http://opds-spec.org/image" type="image/jpeg" />'
                               '<link href="%(modulepath)s?id=99%(item_id)s" rel="x-stanza-cover-image" type="image/jpeg" />'
                               '<link href="%(modulepath)s?id=99%(item_id)s" rel="http://opds-spec.org/thumbnail"  type="image/jpeg" />'
                               '<link href="%(modulepath)s?id=99%(item_id)s" rel="x-stanza-cover-image-thumbnail"  type="image/jpeg" />'
                               )

       self.document_entry_acq_infobook_start='<content type="text/html">'
       self.document_entry_acq_infobook_title='&lt;b&gt;Название книги:&lt;/b&gt; %(e_title)s&lt;br/&gt;'
       self.document_entry_acq_infobook_authors='&lt;b&gt;Авторы:&lt;/b&gt; %(authors)s&lt;br/&gt;'
       self.document_entry_acq_infobook_genres='&lt;b&gt;Жанры:&lt;/b&gt; %(genres)s&lt;br/&gt;'
       self.document_entry_acq_infobook_series='&lt;b&gt;Серии:&lt;/b&gt; %(series)s&lt;br/&gt;'
       self.document_entry_acq_infobook_filename='&lt;b&gt;Файл:&lt;/b&gt; %(filename)s&lt;br/&gt;'
       self.document_entry_acq_infobook_filesize='&lt;b&gt;Размер файла:&lt;/b&gt; %(filesize)sКб.&lt;br/&gt;'
       self.document_entry_acq_infobook_docdate='&lt;b&gt;Дата правки:&lt;/b&gt; %(docdate)s&lt;br/&gt;'
       self.document_entry_acq_infobook_annotation='&lt;p class=book&gt; %(annotation)s&lt;/p&gt;'
       self.document_entry_acq_infobook_userdata=''
       self.document_entry_acq_infobook_finish='</content>'
       self.document_entry_acq_rel_start=''
       self.document_entry_acq_rel_doubles=('<link href="%(modulepath)s?id=23%(item_id)s" rel="related" type="application/atom+xml;profile=opds-catalog" title="Дубликаты книги" />'
                               )
       self.document_entry_acq_rel_authors='%(authors)s %(authors_link)s'
       self.document_entry_acq_rel_genres='%(genres)s'
       self.document_entry_acq_rel_finish=''
       self.document_entry_acq_info_finish=''
       self.document_entry_acq_finish='</entry>'



class webTemplate(opdsTemplate):
    def __init__(self,charset='utf-8'):
       self.response_header=('Content-Type','text/html; charset='+charset)

###################################################################################################################################
# 
# Шаблоны для Агрегации внутри Acquisition Entry
#
# 

       self.agregate_authors=('%(last_name)s %(first_name)s, ')
       self.agregate_authors_link=('<a href="%(modulepath)s?id=22%(author_id)s">%(last_name)s %(first_name)s, </a>'
                               )
       self.agregate_genres='%(genre)s, '
       self.agregate_genres_link=('<a href="%(modulepath)s?id=24%(genre_id)s">%(genre)s</a>, '
                              )
       self.agregate_series='%(ser)s #%(ser_no)s, '
       self.agregate_series_link=('<a href="%(modulepath)s?id=26%(ser_id)s">%%(ser)s</a> #%(ser_no)s, '
                              )

       self.document_page_header_style='''
                           <style>
                               body {font-family: Tahoma, Geneva, sans-serif; font-size: 8pt; color: #000; margin: 0; padding: 20px 20px 20px 20px; }
                               h1 {font-size: 140%%; margin-bottom: 30px; }
                               h2 {font-size: 120%%; }
                               h2 a { color: #000; }
                               a {color: #0F3253;}
                               .page { padding: 5px 5px 5px 5px; }
                               .header {padding-top: 0pt; border-bottom: 2pt dotted #AAA; margin-top: 0pt; line-height=10pt; }
                               .footer {padding-top: 0pt; border-top: 2pt dotted #AAA; margin-top: 0pt; }
                               .navigation_entry  { padding: 0 20px 0 20px; line-height:0; }
                               .navigation_entry h2 { display: inline-block; }
                               .acquisition_entry { padding: 0 20px 0 20px; }
                               .acq_link { clear: both; }
                               .acq_link h2 { display: inline-block; }
                               .acq_cover { float: left; width: 100px; }
                               .acq_infobook  { float: left; width: 600px; }
                               .acq_annotation { font-size: 90%%; }
                               .acq_info_container { clear: both; }
                               .acq_rel { clear: both; }
                            </style>
                            '''
       self.document_page_header=('<html>'
                               '<head>'
                               '<meta charset=%(charset)s>'
                               '<title>%(site_title)s</title>'
                               '%(style)s'
                               '</head>'
                               '<body>'
                               '<div class=page>'
                               '<div class=header><h1>%(page_title)s</h1></div>')
       self.document_page_footer='</div><div class=footer>%(site_subtitle)s</div></body>'
       self.document_mainmenu_std=('<div class=navigation_entry><h2><a href="%(modulepath)s?id=01">По каталогам</a></h2><i>&nbsp;&nbsp;Каталогов: %(cat_num)s, книг: %%(book_num)s.</i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%(alphabet_id)s02">По авторам</a></h2><i>&nbsp;&nbsp;Авторов: %(author_num)s.</i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%(alphabet_id)s03">По наименованию</a></h2><i>&nbsp;&nbsp;Книг: %(book_num)s.</i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=04">По жанрам</a></h2><i>&nbsp;&nbsp;Жанров: %(genre_num)s.</i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%(alphabet_id)s06">По сериям</a></h2><i>&nbsp;&nbsp;Серий: %(series_num)s.</i></div>'
                               )
       self.document_mainmenu_new=('<div class=navigation_entry><h2><a href="%(modulepath)s?id=05">Новинки за %(new_period)s суток.</a></h2><i></i></div>'
                               )
       self.document_mainmenu_shelf=('<div class=navigation_entry><h2><a href="%(modulepath)s?id=08">Книжная полка для %(user)s.</a></h2><i></i></div>'
                               )
       self.document_newmenu=('<entry>'
                               '<title>Все новинки за %(new_period)s суток</title>'
                               '<content type="text">Новых книг: %(newbook_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(alphabet_id)s03&amp;news=1"/>'
                               '<id>id:03:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по авторам</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(alphabet_id)s02&amp;news=1"/>'
                               '<id>id:02:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по Жанрам</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=04&amp;news=1"/>'
                               '<id>id:04:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по Сериям</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%(alphabet_id)s06&amp;news=1"/>'
                               '<id>id:06:news</id></entry>'
                               )
       self.document_authors_submenu=('<div class=navigation_entry><h2><a href="%(modulepath)s?id=31%(author_id)s">Книги по сериям</a></h2><i></i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=34%(author_id)s">Книги вне серий</a></h2><i></i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=33%(author_id)s">Книги по алфавиту</a></h2><i></i></div>'
                               )

       self.document_alphabet_menu=('<div class=navigation_entry><h2><a href="%(modulepath)s?id=%(iid)s&amp;alpha=1%(nl)s">А..Я (РУС)</a></h2><i></i></div>'
                                    '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%(iid)s&amp;alpha=2%(nl)s">0..9 (Цифры)</a></h2><i></i></div>'
                                    '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%(iid)s&amp;alpha=3%(nl)s">A..Z (ENG)</a></h2><i></i></div>'
                                    '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%(iid)s&amp;alpha=4%(nl)s">Другие символы</a></h2><i></i></div>'
                                    '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%(iid)s&amp;alpha=5%(nl)s">Показать все</a></h2><i></i></div>'
                                    )

       self.document_page_control_prev=('<link type="application/atom+xml;profile=opds-catalog;kind=acquisition" rel="prev" title="Previous Page" href="%(modulepath)s?id=%(link_id)s&amp;page=%(page)s" />'
                               )
       self.document_page_control_next=('<link type="application/atom+xml;profile=opds-catalog;kind=acquisition" rel="next" title="Next Page" href="%(modulepath)s?id=%(link_id)s&amp;page=%(page)s" />'
                               )

###############################################################################################################################
#
# Navigation Entry.
#
# В Каждый элемент передаются следующие параметры:
#
# nav_data={'link_id':id,'item_id':item_id,'e_date':reg_date,'e_title':websym(item_title),'e_id':'item:%s'%(item_id),'e_nav_info':'',
#           'nl':self.nl}


       self.document_entry_nav_start='<div class=navigation_entry>\n'
       self.document_entry_nav_title=''
       self.document_entry_nav_link=('<h2><a href="%(modulepath)s?id=%(link_id)s%(nl)s">%(e_title)s</a></h2>'
                               )
       self.document_entry_nav_info=('<i>&nbsp;&nbsp;%(e_nav_info)s</i>')
       self.document_entry_nav_finish='</div>'

###############################################################################################################################
#
# Acquisition Entry.
# 
# В Каждый элемент передаются следующие параметры:
#
# acq_data={'link_id':id,'item_id':item_id,'filename':item_name,'e_date':reg_date,'e_title':websym(item_title),'e_id':'item:%s'%(item_id),
#           'annotation':websym(annotation), 'docdate':docdate, 'format':format,'cover':cover,'cover_type':cover_type,'filesize':fsize//1024,
#           'authors':websym(authors),'genres':websym(genres),'series':websym(series),'authors_link':authors_link,'genres_link':genres_link, 'series_link':series_link,
#           'nl':self.nl}



       self.document_entry_acq_start='<br><div class=acquisition_entry>\n'
       self.document_entry_acq_link_start='<div class=acq_link>'
       self.document_entry_acq_book_title=('<h2>%(e_title)s</h2> <i>Скачать в формате: </i>')
       self.document_entry_acq_book_link_alternate=''
       self.document_entry_acq_book_link=('<i><a href="%(modulepath)s?id=%(id)s%(item_id)s">%(format)s</a></i>&nbsp;'
                               )
       self.document_entry_acq_link_finish='</div>'

       self.document_entry_acq_info_start='<div class=acq_info_container>\n'

       self.document_entry_acq_info_cover=('<div class=acq_cover><img src="%(modulepath)s?id=99%(item_id)s" type="image/jpeg" width="80"></div>'
                               )

       self.document_entry_acq_infobook_start='<div class=acq_infobook>'
       self.document_entry_acq_infobook_title='<b>Название книги:</b> %(e_title)s<br>'
       self.document_entry_acq_infobook_authors='<b>Авторы:</b> %(authors_link)s<br>'
       self.document_entry_acq_infobook_genres='<b>Жанры:</b> %(genres_link)s<br>'
       self.document_entry_acq_infobook_series='<b>Серии:</b> %(series_link)s<br>'
       self.document_entry_acq_infobook_filename='<b>Файл:</b> %(filename)s<br>'
       self.document_entry_acq_infobook_filesize='<b>Размер файла:</b> %(filesize)sКб.<br>'
       self.document_entry_acq_infobook_docdate='<b>Дата правки:</b> %(docdate)s<br>'
       self.document_entry_acq_infobook_annotation='<p class=acq_annotation>%(annotation)s</p>'
       self.document_entry_acq_infobook_userdata=''
       self.document_entry_acq_infobook_finish='</div>'

       self.document_entry_acq_rel_start='<div class=acq_rel>'
       self.document_entry_acq_rel_doubles=('<a href="%(modulepath)s?id=23%(item_id)s">Дубликаты книги "%(e_title)s" (%(dcount)sшт.)</a>'
                               )
       self.document_entry_acq_rel_authors=''
       self.document_entry_acq_rel_genres=''
       self.document_entry_acq_rel_finish='</div>'

       self.document_entry_acq_info_finish='</div>'

       self.document_entry_acq_finish='</div><br>'
