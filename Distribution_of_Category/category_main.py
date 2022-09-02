from Distribution_of_Category.search_category_id import search_category


def distribution(category, api):
    category = category.lower()
    match category:
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
        case ('жіночі купальники' | 'Купальники'):
            return search_category(name_category='Купальники', api=api)
        case ('бюстгалтери'):
            return search_category(name_category='бюстгалтери', api=api)

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

        case ('блузки' | 'жіночі блузки'):
            return search_category(name_category='жіночі блузки', api=api)

        case ('брюки'):
            return search_category(name_category=category, api=api)

        case ('джинси' | 'джинси бойфренди' | 'джинси мом' | 'джинси mom' | 'жіночі джинси'):
            return search_category(name_category='жіночі джинси', api=api)

        case ('жилети' | 'жилетки' | 'жіночі жилетки'):
            return search_category(name_category='жіночі жилети', api=api)

        case ('кардигани' | 'жіночі кардигани'):
            return search_category(name_category='жіночі кардигани', api=api)

        case ('комбінезони' | 'жіночі Комбінезони'):
            return search_category(name_category='жіночі Комбінезони', api=api)

        case ('костюми' | 'брючні костюми' | "в'язані костюми" | 'костюм з шортами' | 'костюми зі спідницею' | 'жіночі костюми'):
            return search_category(name_category='жіночі костюми', api=api)

        case ('жіночі легінси'):
            return search_category(name_category='жіночі легінси', api=api)

        case ('майки' | 'майки жіночі' | 'жіночі майки'):
            return search_category(name_category='жіночі майки', api=api)

        case ('піджаки' | 'жіночі піджаки'):
            return search_category(name_category='жіночі піджаки', api=api)

        case ('поло' | 'жіночі поло'):
            return search_category(name_category='жіночі поло', api=api)

        case ('пляжні накидки'):
            return search_category(name_category=category, api=api)

        case ('сарафани' | 'жіночі сарафани'):
            return search_category(name_category='жіночі сарафани', api=api)

        case ('жіночі батники'):
            return search_category(name_category='жіночі батники', api=api)
        case ("жіночі в'язані светри" | 'светри'):
            return search_category(name_category="жіночі в'язані светри", api=api)
        case ('жіночі водолазки, гольфи' | 'водолазки, гольфи'):
            return search_category(name_category='жіночі водолазки, гольфи', api=api)
        case ('жіночі джемпери'):
            return search_category(name_category='жіночі джемпери', api=api)
        case ('жіночі кофти'):
            return search_category(name_category='жіночі кофти', api=api)
        case ('жіночі толстовки'):
            return search_category(name_category='жіночі толстовки', api=api)
        case ('жіночі світшоти' | 'світшоти'):
            return search_category(name_category=category, api=api)
        case ('жіночі худі'):
            return search_category(name_category='жіночі худі', api=api)

        case ('сорочки' | 'жіночі сорочки'):
            return search_category(name_category='жіночі сорочки', api=api)

        case ('спідниці' | 'жіночі спідниці'):
            return search_category(name_category='жіночі спідниці', api=api)

        case ('сукні' | 'новорічні сукні' | 'плаття на корпоратив' | 'жіночі сукні'):
            return search_category(name_category='жіночі сукні', api=api)

        case ('топи' | 'жіночі топи'):
            return search_category(name_category='жіночі топи', api=api)

        case ('туніки' | 'жіночі туніки'):
            return search_category(name_category='жіночі туніки', api=api)

        case ('футболки' | 'жіночі футболки'):
            return search_category(name_category='жіночі футболки', api=api)

        case ('шорти' | 'жіночі шорти'):
            return search_category(name_category='жіночі шорти', api=api)

        case ('штани' | 'жіночі штани'):
            return search_category(name_category='жіночі штани', api=api)

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
        case ('плащі й тренчи' | 'жіночі зимові куртки' | 'жіночі плащі'):
            return search_category(name_category='жіночі зимові куртки', api=api)
