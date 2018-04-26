package pl.kchmiel;

import com.braintreegateway.*;

import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeFactory;
import javax.xml.datatype.XMLGregorianCalendar;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class Main {
   private static BraintreeGateway gateway;

   public static void main(String[] args) throws DatatypeConfigurationException, ParseException {
      setUp();

//            Customer customer = gateway.customer().find("517093373");
//            String PMtoken = customer.getDefaultPaymentMethod().getToken();


            String PMtoken = "4hx67s";
            Result<PaymentMethodNonce> paymentMethodNonceResult = gateway.paymentMethodNonce().create(PMtoken);
            String nonce = paymentMethodNonceResult.getTarget().getNonce();
            System.out.println(nonce);

//      PaymentMethodRequest paymentMethodRequest = new PaymentMethodRequest();
//      PaymentMethod paymentMethod = gateway.paymentMethod().find("4hx67s");
//      CreditCard creditCard = gateway.creditCard().find(paymentMethod.getToken());
//      System.out.println(creditCard.getMaskedNumber());

//      String mystring = "05/2018";
//      Date thedate = new SimpleDateFormat("MM/yyyy").parse(mystring);
//
//      GregorianCalendar c = new GregorianCalendar();
//      c.setTime(thedate);
//      XMLGregorianCalendar date = DatatypeFactory.newInstance().newXMLGregorianCalendar(c);


      //      TransactionRequest request = new TransactionRequest()
      //            .amount(new BigDecimal("10.00"))
      ////            .paymentMethodToken(token)
      //            .paymentMethodNonce(nonce)
      //            .options()
      //            .submitForSettlement(true)
      //            .done();
      //
      //      Result<Transaction> _result = gateway.transaction().sale(request);

   }

   private static void setUp() {
      gateway = new BraintreeGateway(Environment.SANDBOX, "qtzmqyrvssgxzctq", "htq4q9wb949g2hx4",
            "ff4b75e10c5ee23e734e699568854abb");
   }
}
