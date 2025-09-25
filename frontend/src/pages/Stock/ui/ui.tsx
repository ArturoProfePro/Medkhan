import CurrentPath from '../../../components/CurrentPath/ui/ui';
import Form from '../components/Form/ui/ui';
import c from './ui.module.scss';
import { CheckUpCard } from '../../MainPage/components/Stock/ui/CheckUpCard';
const Stock = () => {
  return (
    <div className={c.container}>
      <CurrentPath />
      <CheckUpCard />
      <Form />
    </div>
  );
};

export default Stock;
