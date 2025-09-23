import c from './ui.module.scss';

const Footer = () => {
  return (
    <footer className={c.container}>
      <div className={c.first}>
        <div className={c.green}>
          <div className={c.left}>
            <img src="/white-logo.png" alt="" />

            <div className={c.mini}>
              <span className={c.ceil}>
                Набережные Челны,
                <br />
                52-й комплекс, 20А
              </span>

              <span className={c.floor}>+7 (901) 143-34-34</span>
            </div>
          </div>

          <div className={c.right}>
            <span className={c.title1}>Пишите нам по любым вопросам</span>

            <div className={c.links}>
              <div className={c.wrapper}>
                <img src="/white-mail.png" />
              </div>
              <div className={c.wrapper}>
                <img src="/white-telegram.png" />
              </div>
              <div className={c.wrapper}>
                <img src="/white-whatsapp.png" />
              </div>
            </div>
          </div>

          <img src="/footer-bg.png" className={c.bg} alt="" />
        </div>

        <div className={c.info}>
          <div className={c.license}>
            <span className={c.title2}>
              Лицензия на медицинскую деятельность
            </span>

            <span className={c.desc}>проверить лицензию</span>
          </div>

          <div className={c.blocks}>
            <div className={c.block}>
              <span className={c.title3}>4.9</span>
              <img src="/yandex.png" alt="" />
            </div>
            <div className={c.block}>
              <span className={c.title3}>4.7</span>
              <img src="/2gis.png" alt="" />
            </div>
          </div>
        </div>
      </div>

      <div className={c.second}>
        <div className={c.block}>
          <img src="/original-telegram.png" alt="" />
          <span>MedKhan в тг</span>
        </div>
        <div className={c.block}>
          <img src="/original-wk.png" alt="" />
          <span>MedKhan в вк</span>
        </div>
        <div className={c.block}>
          <img src="/original-youtube.png" alt="" />
          <span>MedKhan в youtube</span>
        </div>
      </div>

      <div className={c.third}>
        <span className={c.ceil}>
          © 2023 - 2025 г. «Медицинский центр МедХан»
        </span>

        <div className={c.floor}>
          <span className={c.bir}>Политика конфиденциальности</span>
          <span className={c.eki}>Реквизиты</span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
