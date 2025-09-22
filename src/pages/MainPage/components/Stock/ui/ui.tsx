import c from './ui.module.scss';

const Stock = () => {
  return (
    <div className={c.container}>
      <div className={c.header}>
        <span className={c.title}>Акции</span>

        <span className={c.button}>
          <img src="/arrow-right-black.svg" className={c.arrow} />
        </span>
      </div>

      <div className={c.grid}>
        <div className={[c.elem1, c.elem].join(' ')}>
          <img src="/girl.png" className={c.girl} />
          <img src="/girl-bg.png" className={c.bg} />

          <div className={c.modal}>
            <span className={c.ceil}>до 5 марта</span>
            <span className={c.floor}>-15%</span>
          </div>

          <div className={c.info}>
            <div className={c.price}>
              <span className={c.ceil}>6 000 ₽</span>
              <span className={c.floor}>7 200 ₽</span>
            </div>

            <span className={c.title}>CHECK UP</span>
            <span className={c.desc}>
              «Боль в спине
              <br />
              Расширенный»
            </span>
          </div>
        </div>

        <div className={[c.elem2, c.elem].join(' ')}>
          <img src="/packet-s.png" className={c.ch} />
          <img src="/packet-s-bg.png" className={c.bg} />

          <div className={c.modal}>
            <span className={c.ceil}>до 5 марта</span>
            <span className={c.floor}>-15%</span>
          </div>

          <div className={c.info}>
            <div className={c.price}>
              <span className={c.ceil}>6 000 ₽</span>
              <span className={c.floor}>7 200 ₽</span>
            </div>

            <span className={c.title}>CHECK UP</span>
            <span className={c.desc}>«Женское здоровье» (Пакет S)</span>
          </div>
        </div>

        <div className={[c.elem3, c.elem].join(' ')}>
          <div className={c.modal}>
            <span className={c.ceil}>до 5 марта</span>
            <span className={c.floor}>-15%</span>
          </div>

          <div className={c.info}>
            <div className={c.price}>
              <span className={c.ceil}>6 000 ₽</span>
              <span className={c.floor}>7 200 ₽</span>
            </div>

            <span className={c.title}>CHECK UP</span>
            <span className={c.desc}>«Репродуктивность»</span>
          </div>
        </div>

        <div className={[c.elem4, c.elem].join(' ')}>
          <div className={c.modal}>
            <span className={c.ceil}>до 5 марта</span>
            <span className={c.floor}>-15%</span>
          </div>

          <div className={c.info}>
            <div className={c.price}>
              <span className={c.ceil}>6 000 ₽</span>
              <span className={c.floor}>7 200 ₽</span>
            </div>

            <span className={c.title}>CHECK UP</span>
            <span className={c.desc}>«Здоровый желудок»</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Stock;
