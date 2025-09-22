import c from './ui.module.scss'

const News = () => {

    return (
        <div className={c.container}>
            <div className={c.main}>
                <div className={c.part}>
                    <span className={c.title}>СМИ о нас</span>
                    <span className={c.desc}>Здесь можете ознакомиться с опубликованными статьями</span>

                </div>
                <button className={c.button}>Все статьи <img src='/arrow-right-black.svg' /></button>
            </div>

            <div className={c.list}>
                <div className={c.block}>
                    <span className={c.title}>Название статьи</span>

                    <div className={c.wrapper}><img src='/bo.svg' /></div>
                </div>
                <div className={c.block}>
                    <span className={c.title}>Название статьи</span>

                    <div className={c.wrapper}><img src='/chi.svg' /></div>
                </div>
                <div className={c.block}>
                    <span className={c.title}>Название статьи</span>

                    <div className={c.wrapper}><img src='/dzen.svg' /></div>
                </div>
            </div>
        </div>
    )
}

export default News