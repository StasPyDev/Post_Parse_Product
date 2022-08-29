from Distribution_of_Category.search_category_id import search_category


def distribution(category, api):
    category = category.lower()
    match category:
        case ('боді'):
            return search_category(name_category=category, api=api)
        case ('жіночі колготки'):
            return search_category(name_category=category, api=api)
        case ('жіночі піжами' | 'піжамі'):
            return search_category(name_category=category, api=api)
        case ('жіночі труси'):
            return search_category(name_category=category, api=api)
        case ('жіночі шкарпетки'):
            return search_category(name_category=category, api=api)
        case ('комплекти жіночої білизни'):
            return search_category(name_category='комплекти жіночої білизни', api=api)
        case ('жіночі купальники'):
            return search_category(name_category=category, api=api)

        case ('жіночі спортивний костюм'):
            return search_category(name_category=category, api=api)
        case ('жіночі спортивний лосини'):
            return search_category(name_category=category, api=api)
        case ('жіночі спортивний майки'):
            return search_category(name_category=category, api=api)
        case ('жіночі спортивний топи'):
            return search_category(name_category=category, api=api)
        case ('жіночі спортивний шорти'):
            return search_category(name_category=category, api=api)
        case ('жіночі спортивний штани'):
            return search_category(name_category=category, api=api)

        case ('блузки'):
            return search_category(name_category=category, api=api)

        case ('брюки'):
            return search_category(name_category=category, api=api)

        case ('джинси' | 'джинси бойфренди' | 'джинси мом' | 'джинси mom'):
            return search_category(name_category=category, api=api)

        case ('жилети' | 'жилетки' | 'жіночі жилетки'):
            return search_category(name_category='жіночі жилетки', api=api)

        case ('кардигани' | 'жіночі кардигани'):
            return search_category(name_category='жіночі кардигани', api=api)

        case ('комбінезони'):
            return search_category(name_category=category, api=api)

        case ('костюми' | 'брючні костюми' | "в'язані костюми" | 'костюм з шортами' | 'костюми зі спідницею'):
            return search_category(name_category=category, api=api)

        case ('жіночі легінси'):
            return search_category(name_category=category, api=api)

        case ('майки' | 'майки жіночі' | 'жіночі майки'):
            return search_category(name_category='жіночі майки', api=api)

        case ('піджаки'):
            return search_category(name_category=category, api=api)

        case ('поло'):
            return search_category(name_category=category, api=api)

        case ('пляжні накидки'):
            return search_category(name_category=category, api=api)

        case ('сарафани'):
            return search_category(name_category=category, api=api)

        case ('жіночі батники'):
            return search_category(name_category=category, api=api)
        case ("жіночі в'язані светри" | 'светри'):
            return search_category(name_category=category, api=api)
        case ('жіночі водолазки, гольфи' | 'водолазки, гольфи'):
            return search_category(name_category=category, api=api)
        case ('жіночі джемпери'):
            return search_category(name_category=category, api=api)
        case ('жіночі кофти'):
            return search_category(name_category=category, api=api)
        case ('жіночі толстовки'):
            return search_category(name_category=category, api=api)
        case ('жіночі світшоти' | 'світшоти'):
            return search_category(name_category=category, api=api)
        case ('жіночі худі'):
            return search_category(name_category=category, api=api)

        case ('сорочки'):
            return search_category(name_category=category, api=api)

        case ('спідниці'):
            return search_category(name_category=category, api=api)

        case ('сукні' | 'новорічні сукні' | 'плаття на корпоратив'):
            return search_category(name_category='сукні', api=api)

        case ('топи'):
            return search_category(name_category=category, api=api)

        case ('туніки'):
            return search_category(name_category=category, api=api)

        case ('футболки' | 'жіночі футболки'):
            return search_category(name_category='жіночі футболки', api=api)

        case ('шорти' | 'жіночі шорти'):
            return search_category(name_category='шорти', api=api)

        case ('штани'):
            return search_category(name_category=category, api=api)

        case ('жіночі бомбери' | 'вітровки' | 'куртки'):
            return search_category(name_category=category, api=api)
        case ('жіночі демісезонні куртки' | 'парки'):
            return search_category(name_category=category, api=api)
        case ('жіночі джинсові куртки' | 'джинсові куртки'):
            return search_category(name_category=category, api=api)
        case ('жіночі пальто' | 'пальто'):
            return search_category(name_category=category, api=api)
        case ('жіночі шкіряні куртки' | 'косухи шкіряні жіночі'):
            return search_category(name_category=category, api=api)
        case ('жіночі шуби' | 'шуби'):
            return search_category(name_category=category, api=api)
        case ('плащі й тренчи'):
            return search_category(name_category=category, api=api)
