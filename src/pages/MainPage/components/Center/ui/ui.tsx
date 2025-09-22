import c from './ui.module.scss'

const Center = () => {

    return (
        <div className={c.container}>
            <div className={c.info}>
                <span className={c.title}>
                    Медицинский центр <br />МедХан
                </span>
                <span className={c.desc}>Многопрофильное медицинское учреждение, предлагающее специально подобранный комплекс процедур для каждого клиента. В работе клиники все построено с учетом максимального комфорта для посетителей. Новейшее оборудование центра позволяет провести диагностику организма пациента для составления плана лечения и профилактических мероприятий.</span>
            </div>

            <img src="/center.png" className={c.img} alt="" />

            <div className={c.list}>

                <div className={c.block}>
                    <span className={c.title}>100</span>
                    <span className={c.desc}>Профессионалов в сфере<br />медицины</span>
                    <img src="/energy.svg" className={c.icon} alt="" />
                </div>

                <div className={c.block}>
                    <span className={c.title}>50</span>
                    <span className={c.desc}>Профессионалов в сфере</span>
                    <img src="/molecula.svg" className={c.icon} alt="" />
                </div>

                <div className={c.block}>
                    <span className={c.title}>6</span>
                    <span className={c.desc}>Лет заботимся о Вас</span>
                    <img src="/flower.svg" className={c.icon} alt="" />
                </div>

                <div className={c.block}>
                    <span className={c.title}>6</span>
                    <span className={c.desc}>Дней в неделю следим<br />за вашим здоровьем<br />медицины</span>
                    <img src="/heart.svg" className={c.icon} alt="" />
                </div>
            </div>
        </div>
    )
}

export default Center