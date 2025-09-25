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
          console.log(item.checkup_type);
          switch (item.checkup_type) {
            case 'FIRST':
              return (
                <div className={c.mainCard}>
                  {' '}
                  <CheckUpFirst key={item.id} {...item} />
                </div>
              );
            case 'SECONDARY':
              return <CheckUpSeconde key={item.id} {...item} />;
            case 'THIRD':
              return <CheckUpThird key={item.id} {...item} />;
          }
        })}
      </div>
    </>
  );
};
