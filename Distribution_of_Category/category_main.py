from Distribution_of_Category.search_category_id import search_category


def distribution(category, api):
    for categorie in category:
        category = categorie
    category = category.lower()
    match category:
        # Жіноча білизна
        case ('боді'):
            return search_category(name_category='боді', api=api)
        case ('жіночі колготки'):
            return search_category(name_category='жіночі колготки', api=api)
        case ('жіночі піжами' | 'піжамі'):
            return search_category(name_category='жіночі піжами', api=api)
        case ('жіночі труси'):
            return search_category(name_category='жіночі труси', api=api)
        case ('жіночі шкарпетки'):
            return search_category(name_category='жіночі шкарпетки', api=api)
        case ('комплекти жіночої білизни'):
            return search_category(name_category='комплекти жіночої білизни', api=api)
        case ('жіночі купальники' | 'купальники'):
            return search_category(name_category='купальники', api=api)
        case ('бюстгалтери'):
            return search_category(name_category='бюстгалтери', api=api)
        # Жіночий спортивний одяг
        case ('жіночі спортивний костюм' | 'жіночі спортивні костюми'):
            return search_category(name_category='жіночі спортивні костюми', api=api)
        case ('жіночі спортивний лосини'):
            return search_category(name_category=category, api=api)
        case ('жіночі спортивний майки' | 'жіночі спортивні майки'):
            return search_category(name_category='жіночі спортивні майки', api=api)
        case ('жіночі спортивний топи' | 'жіночі спортивні топи'):
            return search_category(name_category='жіночі спортивні топи', api=api)
        case ('жіночі спортивний шорти' | 'жіночі спортивні шорти'):
            return search_category(name_category='жіночі спортивні шорти', api=api)
        case ('жіночі спортивний штани' | 'жіночі спортивні штани'):
            return search_category(name_category='жіночі спортивні штани', api=api)
        case ('жіночі спортивні рашгарди, лонгсліви'):
            return search_category(name_category='жіночі спортивні рашгарди, лонгсліви', api=api)
        # Жіночі блузки
        case ('блузки' | 'жіночі блузки'):
            return search_category(name_category='жіночі блузки', api=api)
        #
        case ('брюки'):
            return search_category(name_category='брюки', api=api)
        # Жіночі джинси
        case ('джинси' | 'джинси бойфренди' | 'джинси мом' | 'джинси mom' | 'жіночі джинси'):
            return search_category(name_category='жіночі джинси', api=api)
        # Жіночі жилети
        case ('жилети' | 'жилетки' | 'жіночі жилетки'):
            return search_category(name_category='жіночі жилети', api=api)
        # Жіночі кардигани
        case ('кардигани' | 'жіночі кардигани'):
            return search_category(name_category='жіночі кардигани', api=api)
        # Жіночі Комбінезони
        case ('комбінезони' | 'жіночі Комбінезони'):
            return search_category(name_category='жіночі Комбінезони', api=api)
        # Жіночі костюми
        case ('костюми' | 'костюми, комбінезони' | 'брючні костюми' | "в'язані костюми" | 'костюм з шортами' | 'костюми зі спідницею' | 'жіночі костюми'):
            return search_category(name_category='жіночі костюми', api=api)
        # Жіночі лосини
        case ('жіночі легінси'):
            return search_category(name_category='жіночі легінси', api=api)
        # Жіночі майки
        case ('майки' | 'майки жіночі' | 'жіночі майки'):
            return search_category(name_category='жіночі майки', api=api)
        # Жіночі піджаки
        case ('піджаки' | 'жіночі піджаки'):
            return search_category(name_category='жіночі піджаки', api=api)
        # Жіночі поло
        case ('поло' | 'жіночі поло'):
            return search_category(name_category='жіночі поло', api=api)
        # пляжні накидки
        case ('пляжні накидки'):
            return search_category(name_category='пляжні накидки', api=api)
        # Жіночі сарафани
        case ('сарафани' | 'жіночі сарафани'):
            return search_category(name_category='жіночі сарафани', api=api)
        # Жіночі светри, світшоти, худі
        case ('жіночі батники'):
            return search_category(name_category='жіночі батники', api=api)
        case ("жіночі в'язані светри" | 'светри'):
            return search_category(name_category="жіночі в'язані светри", api=api)
        case ('жіночі водолазки, гольфи' | 'водолазки, гольфи'):
            return search_category(name_category='жіночі водолазки, гольфи', api=api)
        case ('жіночі джемпери'):
            return search_category(name_category='жіночі джемпери', api=api)
        case ('жіночі кофти' | 'кофти'):
            return search_category(name_category='жіночі кофти', api=api)
        case ('жіночі толстовки'):
            return search_category(name_category='жіночі толстовки', api=api)
        case ('жіночі світшоти' | 'світшоти'):
            return search_category(name_category='жіночі світшоти', api=api)
        case ('жіночі худі'):
            return search_category(name_category='жіночі худі', api=api)
        # Жіночі сорочки
        case ('сорочки' | 'жіночі сорочки'):
            return search_category(name_category='жіночі сорочки', api=api)
        # Жіночі спідниці
        case ('спідниці' | 'жіночі спідниці'):
            return search_category(name_category='жіночі спідниці', api=api)
        # Жіночі сукні
        case ('сукні' | 'новорічні сукні' | 'плаття на корпоратив' | 'жіночі сукні' | 'плаття'):
            return search_category(name_category='жіночі сукні', api=api)
        # Жіночі топи
        case ('топи' | 'жіночі топи'):
            return search_category(name_category='жіночі топи', api=api)
        # Жіночі туніки
        case ('туніки' | 'жіночі туніки'):
            return search_category(name_category='жіночі туніки', api=api)
        # Жіночі футболки
        case ('футболки' | 'жіночі футболки' | 'футболки, майки'):
            return search_category(name_category='жіночі футболки', api=api)
        # Жіночі шорти
        case ('шорти' | 'жіночі шорти'):
            return search_category(name_category='жіночі шорти', api=api)
        # Жіночі штани
        case ('штани' | 'жіночі штани'):
            return search_category(name_category='жіночі штани', api=api)
        # Верхній одяг для жінок
        case ('жіночі бомбери' | 'вітровки' | 'куртки' | 'Жіночі вітровки'):
            return search_category(name_category='жіночі вітровки', api=api)
        case ('жіночі демісезонні куртки' | 'парки' | 'жіночі парки'):
            return search_category(name_category='жіночі парки', api=api)
        case ('жіночі джинсові куртки' | 'джинсові куртки'):
            return search_category(name_category='жіночі джинсові куртки', api=api)
        case ('жіночі пальто' | 'пальто'):
            return search_category(name_category='жіночі пальто', api=api)
        case ('жіночі шкіряні куртки' | 'косухи шкіряні жіночі'):
            return search_category(name_category='жіночі шкіряні куртки', api=api)
        case ('жіночі шуби' | 'шуби'):
            return search_category(name_category='жіночі шуби', api=api)
        case ('плащі й тренчи' | 'жіночі зимові куртки' | 'жіночі плащі' | 'верхній одяг'):
            return search_category(name_category='жіночі зимові куртки', api=api)

        # Дитячий одяг
        case ('дитячі сукні'):
            return search_category(name_category='дитячі сукні', api=api)
        case ('дитячі сорочки, блузи'):
            return search_category(name_category='дитячі сорочки, блузи', api=api)
        case ('дитячі костюми'):
            return search_category(name_category='дитячі костюми', api=api)
        case ('дитячі пальто, жилети'):
            return search_category(name_category='дитячі пальто, жилети', api=api)

        # Family look
        case ('family look' | 'дитячий одяг по 99 грн' | 'дитячий одяг по 199 грн' | 'дитячий одяг по 699 грн'):
            return search_category(name_category='family look', api=api)

        # Аксесуари
        case('біжутерія'):
            return search_category(name_category='біжутерія', api=api)
        case ('жіночі сумки' | 'аксесуари'):
            return search_category(name_category='жіночі сумки', api=api)

        # Взуття жіноче
        case('сапоги'):
            return search_category(name_category='сапоги', api=api)
        case ('черевики'):
            return search_category(name_category='черевики', api=api)
        case ('лофери'):
            return search_category(name_category='лофери', api=api)
        case ('кеди'):
            return search_category(name_category='кеди', api=api)

        # Взуття чоловіче
        case('сапоги'):
            return search_category(name_category='сапоги', api=api)
        case ('черевики'):
            return search_category(name_category='черевики', api=api)
        case ('лофери'):
            return search_category(name_category='лофери', api=api)
        case ('кеди'):
            return search_category(name_category='кеди', api=api)
