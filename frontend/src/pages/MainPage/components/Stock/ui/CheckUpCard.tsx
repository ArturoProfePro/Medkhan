import { useCheckUps } from '../../../../../hooks/useCheckUps';
import c from './ui.module.scss';
import { CheckUpFirst } from './CheckUpTypes/CheckUpFirst';
import { CheckUpSeconde } from './CheckUpTypes/CheckUpSeconde';
import { CheckUpThird } from './CheckUpTypes/CheckUpThird';
export const CheckUpCard = () => {
  const { data, isLoading, error } = useCheckUps();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading check-ups</div>;
  if (!data?.data?.length) return <div>No check-ups found</div>;
  return (
    <>
      <div className={c.grid}>
        {data.data.map((item) => {
          switch (item.CheckUpType) {
            case 'first':
              return <CheckUpFirst key={item.id} {...item} />;
            case 'seconde':
              return <CheckUpSeconde key={item.id} {...item} />;
            case 'third':
              return <CheckUpThird key={item.id} {...item} />;
            default:
              return <CheckUpSeconde key={item.id} {...item} />;
          }
        })}
      </div>
    </>
  );
};
