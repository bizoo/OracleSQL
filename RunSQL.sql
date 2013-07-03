SET LINESIZE 2000
SET PAGESIZE 0
SET VERIFY OFF
SET FEEDBACK OFF
@&1
SELECT 'Filename: &1' FROM DUAL;
SELECT '(' || TYPE || ' ' || NAME || '/0:' || POSITION || ')' || ' ' || LINE || ':' || POSITION || ' ' || TEXT as ERRORS
  FROM USER_ERRORS
 WHERE line <> 0
   AND TYPE || ' ' || NAME in (&2)
ORDER BY NAME, TYPE, SEQUENCE;
exit
