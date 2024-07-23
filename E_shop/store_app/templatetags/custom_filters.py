from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    try:
        value = float(value)
        return '{:,.0f}₫'.format(value).replace(',', '.')  # Định dạng giá trị thành tiền Việt Nam, dùng dấu chấm ngăn cách phần ngàn
    except (ValueError, TypeError):
        return value  # Trả về giá trị ban đầu nếu không thể chuyển đổi