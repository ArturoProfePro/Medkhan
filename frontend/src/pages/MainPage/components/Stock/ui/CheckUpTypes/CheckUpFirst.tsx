import c from './Styles/First.module.scss';
import common from './Styles/Common.module.scss';
import { CheckUp } from '../../../../../../Interface/CheckUps.interface';

type CheckUpFirstType = CheckUp;

export const CheckUpFirst = ({
  discountedPrice,
  gender,
  name,
  originalPrice,
  discountPercentage,
  expiredAt,
}: CheckUpFirstType) => {
  return (
    <>
      <div className={`${common.card} ${c.card}`}>
        <div className={c.leftContent}>
          <div className={c.top}>
            <img
              src={
                gender === 'general'
                  ? '/gender-gray.png'
                  : gender === 'women'
                  ? '/girl-gender.png'
                  : '/boy-gender.png'
              }
              alt="gender"
            />
            <div>
              <span>до {expiredAt}</span>
              <span>-{discountPercentage}%</span>
            </div>
          </div>
          <div className={c.middle}>
            <div>
              {discountedPrice && <span>{discountedPrice} ₽</span>}
              <span className={discountedPrice ? common.lineThrough : ''}>
                {originalPrice} ₽
              </span>
            </div>
            <div>
              <span>CHECK UP</span>
              <span>{name}</span>
            </div>
          </div>
        </div>
        <div className={c.rightImage}>
          <img src="/girl.png" alt="Девушка" className={c.girl} />
          <img src="/girl-bg.png" alt="Фон" className={c.bgGirl} />
        </div>
      </div>
    </>
  );
};
