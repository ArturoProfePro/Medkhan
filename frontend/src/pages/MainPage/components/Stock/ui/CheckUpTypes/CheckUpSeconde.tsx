import c from './Styles/Seconde.module.scss';
import common from './Styles/Common.module.scss';
import { CheckUp } from '../../../../../../Interface/CheckUps.interface';

type CheckUpFirstType = CheckUp;

export const CheckUpSeconde = ({
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
        <div className={common.top}>
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
        <div className={common.middle}>
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
        <img src="/zelenaya-shtuka.png" alt="" className={c.bggGreen} />
      </div>
    </>
  );
};
