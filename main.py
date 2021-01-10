from core import getPollutionData, Visualizor, Config, MeasureTracker
from requests import post

if __name__ == '__main__':
    config = Config()
    tracker = MeasureTracker()

    data = getPollutionData(config.iqair_api_key, config.country, config.province, config.city)
    info = Visualizor(data, True)

    if info.aqi != tracker.last_measure:
        info.generateImage()
        info.generateCaption()
        post(f'https://api.telegram.org/bot{config.telegram_api_key}/sendPhoto', data={'chat_id': config.telegram_chat_id, 'caption': info.caption, 'disable_notifications': True}, files={'photo': info.imageb})
        tracker.setMeasure(info.aqi)