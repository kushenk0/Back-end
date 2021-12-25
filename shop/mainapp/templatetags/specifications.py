from django import template
from django.utils.safestring import mark_safe


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Діагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Частота процесора': 'processor_freq',
        "Оперативна пам'ять": 'ram',
        'Відеокарта': 'video',
        'Час роботи акумулятора': 'time_without_charge'
    },
    'smartphone': {
        'Діагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Роздільна здатність відео': 'resolution',
        "Об'єм акумулятора": 'accum_volume',
        "Об'єм вбудовуваної пам'яті": 'ram',
        # 'Нявність слота для SD карти': 'sd',
        # "Об'єм вбудовуваної пам'яті": 'sd_volume_max',
        'Оновна камера': 'main_cam_mp',
        'Фронтальна камера': 'frontal_cam_mp'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)


