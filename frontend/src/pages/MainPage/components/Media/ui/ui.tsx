import c from './ui.module.scss'

const Media = () => {

    return (
        <div className={c.container}>
            <div className={c.main}>
                <span className={c.title}>Медиа</span>
                <div className={c.links}>
                    <span className={c.title}>Присоединяйтесь:</span>
                    <div className={c.list}>
                        <div className={c.wrapper}><img src='/youtube.png' /></div>
                        <div className={c.wrapper}><img src='/telegram.png' /></div>
                        <div className={c.wrapper}><img src='/instagram.png' /></div>
                    </div>
                </div>
            </div>

            <div className={c.list}>
                <div className={c.block}>
                    <img src="/first-video.png" alt="" />
                </div>
                <div className={c.block}>
                    <img src="/second-video.png" alt="" />
                </div>
                <div className={c.block}>
                    <img src="/third-video.png" alt="" />
                </div>
            </div>
        </div>
    )
}

export default Media