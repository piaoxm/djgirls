# Custom Path Converter

# converters.py ------------ 앱폴더나 프로젝트폴더에 만들면됨.
class FourDigitYearConverter:
    regex = r'[0-9]{4}'
    def to_python(self, value): # url로부터 추출한 문자열을 뷰에 넘겨주기 전에 변환
        return int(value)
    def to_url(self, value): # url reverse시에 호출
        return '%04d' % value

