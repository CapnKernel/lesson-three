## The If Template Tag

* We could also use `if` and `else` template tag to control the content of the template

* For example:

```
<html>
    <head>
        <title>Albums</title>
    </head>
    <body>
    {% if albums %}
        {% for album in albums %}  
        <tr>
            <td> <a href="album/{{album.id}}"> {{ album.name }} </a> </td>
            <td> {{ album.tracks }} </td>
            <td> {{ album.length }} </td>
        </tr>
        {% endfor %}
    {% else %}
        <p> Add your favorite albums </p>
    {% endif %}                        
    </body>
<html>

## 'album/album_list.html'   
```