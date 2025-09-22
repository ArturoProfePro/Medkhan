import { useRef } from 'react'
import c from './ui.module.scss'
import { CSSTransition } from 'react-transition-group'
import { Link } from 'react-router';
import './ui.transition.scss'

const Storm = ({ isOpen }: { isOpen: boolean }) => {
    const containerRef = useRef<HTMLDivElement | null>(null);

    return (
        <CSSTransition
            mountOnEnter
            unmountOnExit
            classNames="storm"
            in={isOpen}
            nodeRef={containerRef}
            timeout={200}
        >
        <div ref={containerRef} className={c.container}>
            <div className={c.wrapper}>
                <img src="/loop.svg" alt="" />
                <input placeholder='Поиск по названию услуги' className={c.input} />
            </div>

            <nav className={c.nav}>
                <Link to="/services" className={c.elem}>Услуги</Link>
                <Link to="/stock" className={c.elem}>Акции</Link>
                <Link to="/specialists" className={c.elem}>Специалисты</Link>
                <Link to="/reviews" className={c.elem}>Отзывы</Link>
                <Link to="/contacts" className={c.elem}>Контакты</Link>
            </nav>

            <span className={c.phone}>+7 (901) 143-34-34</span>

            <span className={c.title}>Часы работы</span>

            <span className={c.desc}><span className={c.wow}>Пн-Пт</span> с 7:00 до 19:00 </span>
            <span className={c.desc}><span className={c.wow}>Сб</span> с 8:00 до 16:00 </span>
            <span className={c.desc}><span className={c.wow}>Вс</span> с 8:00 до 14:00</span>
        </div>
        </CSSTransition>
    )
}

export default Storm