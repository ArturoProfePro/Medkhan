import c from './ui.module.scss'

const SpecialistList = () => {

    return (
        <div className={c.container}>
            <div className={c.header}>
                <span className={c.title}>Команда специалистов</span>

                <div className={c.options}>
                    <div className={c.wrapper}>
                        Пол
                        <img src="/arrow-bottom.svg" alt="" />
                    </div>

                    <div className={c.wrapper}>
                        Специализация
                        <img src="/arrow-bottom.svg" alt="" />
                    </div>

                    <div className={c.wrapper2}>
                        <img src="/loop.svg" alt="" />
                        <input placeholder='Поиск по названию услуги' className={c.input} />
                    </div>
                </div>
            </div>

            <div className={c.filters}>
                <div className={c.filter}>Уролог <img src="/x.svg" className={c.x} alt="" /></div>

                <div className={c.alpha}>
                    <span className={c.all}>Все</span>
                    А   Б  В  Г  Д   Е   Ё   Ж   З   И   К   Л   М   Н   О   П   Р   С   Т   У   Ф   Х   Ц   Ч   Ш   Щ   Ъ   Ы   Ь   Э   Ю   Я
                </div>
            </div>

            <div  className={c.grid}>
                <div className={c.block}>
                    <div className={c.wrapper}>
                        <img src="/first-doctor.png" alt="" />
                        <div className={c.exp}>Стаж 31 год</div>
                    </div>

                    <div className={c.info}>
                        <span className={c.name}>Нудельман <br/>Наталия Федоровна</span> 
                        <span className={c.job}>Врач-невролог</span>

                        <button className={c.button}>Записаться</button>
                    </div>
                </div>

                
                <div className={c.block}>
                    <div className={c.wrapper}>
                        <img src="/second-doctor.png" alt="" />
                        <div className={c.exp}>Стаж 25 лет</div>
                    </div>

                    <div className={c.info}>
                        <span className={c.name}>Хан<br/>Умар Хаят</span> 
                        <span className={c.job}>Андролог, главный врач, уролог</span>

                        <button className={c.button}>Записаться</button>
                    </div>
                </div>


                <div className={c.block}>
                    <div className={c.wrapper}>
                        <img src="/third-doctor.png" alt="" />
                        <div className={c.exp}>Стаж 27 лет</div>
                    </div>

                    <div className={c.info}>
                        <span className={c.name}>Хан<br/>Тюльпан Тимергалиевна</span> 
                        <span className={c.job}>Акушер-гинеколог, врач УЗИ, генеральный директор, гинеколог</span>

                        <button className={c.button}>Записаться</button>
                    </div>
                </div>


                <div className={c.block}>
                    <div className={c.wrapper}>
                        <img src="/fourth-doctor.png" alt="" />
                        <div className={c.exp}>Стаж 15 лет</div>
                    </div>

                    <div className={c.info}>
                        <span className={c.name}>Башарова<br/>Альбина Шарипзяновна</span> 
                        <span className={c.job}>Врач УЗИ, врач функциональной диагностики, кардиолог, терапевт</span>

                        <button className={c.button}>Записаться</button>
                    </div>
                </div>


                <div className={c.block}>
                    <div className={c.wrapper}>
                        <img src="/fifth-doctor.png" alt="" />
                        <div className={c.exp}>Стаж 6 лет</div>
                    </div>

                    <div className={c.info}>
                        <span className={c.name}>Мартьянов <br/>Иван Сергеевич</span> 
                        <span className={c.job}>Хирург</span>

                        <button className={c.button}>Записаться</button>
                    </div>
                </div>


                <div className={c.block}>
                    <div className={c.wrapper}>
                        <img src="/sixth-doctor.png" alt="" />
                        <div className={c.exp}>Стаж 14 лет</div>
                    </div>

                    <div className={c.info}>
                        <span className={c.name}>Юлдашев <br/>Фарход Талибович</span> 
                        <span className={c.job}>Проктолог, эндоскопист</span>

                        <button className={c.button}>Записаться</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SpecialistList